import os
from datetime import datetime as dt
from dotenv import load_dotenv
import werkzeug
from werkzeug.security import check_password_hash
from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap5
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, selectinload
from database import init_db, User, Blog, Comment
from forms import BlogForm, ContactForm, RegisterForm, LoginForm, CommentForm
from functions import send_mail

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


db_engine = init_db()
Session = sessionmaker(bind=db_engine, future=True)


bootstrap = Bootstrap5(app)

# Flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    with Session() as session:
        return session.get(User, int(user_id))


# Decorators
def admin_only(func):
    def wrapper(*args, **kwargs):
        post_id = kwargs.get("post_id")
        with Session() as session:
            this_post = session.get(Blog, post_id)
            if this_post and current_user.id != this_post.author_id:
                return redirect("/")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


def admin_or_creator_only(func):
    def wrapper(*args, **kwargs):
        comment_id = kwargs.get("comment_id")
        with Session() as session:
            this_comment = session.get(Comment, comment_id)
            if this_comment and current_user.id not in [this_comment.author_id, this_comment.post.author_id]:
                return redirect("/")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


# Huvudsida – visar de senaste 6 inläggen
@app.route("/", methods=["GET"])
def home():
    url_blog = url_for("blog")
    with Session() as session:
        # Eager load author för att undvika DetachedInstanceError
        newest_posts = session.execute(
            select(Blog)
            .options(selectinload(Blog.author))
            .order_by(Blog.date.desc())
            .limit(6)
        ).scalars().all()
    return render_template("index.html", url_blog=url_blog, posts=newest_posts)





# Registrera användare
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        with Session() as session:
            existing_user = session.execute(
                select(User).where(User.email == form.email.data)).scalar_one_or_none()
            if existing_user:
                flash("Något gick fel")
            else:
                hashed_password = werkzeug.security.generate_password_hash(
                    form.password.data, method="scrypt", salt_length=8
                )
                new_user = User(
                    email=form.email.data.lower(),
                    name=form.name.data,
                    password=hashed_password
                )
                session.add(new_user)
                session.commit()
                return redirect(url_for("login"))

    return render_template("form-page.html", form=form, input_video="./static/videos/blogpage.mp4", input_text="Skapa konto")




# Logga in Användare
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with Session() as session:

            user = session.execute(select(User).where(User.email == form.email.data.lower())).scalar()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Något gick fel - Prova igen")
    return render_template("form-page.html", form=form, input_video="./static/videos/blogpage.mp4", input_text="Logga in")


# Logga ut användare
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Användare utloggad")
    return redirect("/login")







# Bloggsida – lista alla inlägg för en användare
@app.route("/blog", methods=["GET"])
@login_required
def blog():
    url_blog = url_for("blog")
    with Session() as session:
        blog_posts = session.execute(
            select(Blog)
            .options(selectinload(Blog.comments))
            .where(Blog.author_id == current_user.id)
        ).scalars().all()
    return render_template("blog.html", posts=blog_posts, url_blog=url_blog, input_video="./static/videos/blogpage.mp4", input_text=f"{current_user.name.title()}s - Blogg")



# Visa ett enskilt blogginlägg
@app.route("/blog/<int:post_id>", methods=["GET", "POST"])
def blog_post(post_id):
    form = CommentForm()
    with Session() as session:
        post = session.execute(
            select(Blog)
            .options(
                selectinload(Blog.comments).selectinload(Comment.author),
                selectinload(Blog.author)
            )
            .where(Blog.id == post_id)
        ).scalar_one_or_none()

        if not post:
            flash("Inlägget hittades inte")
            return redirect("/blog")

        if form.validate_on_submit():
            new_comment = Comment(
                author_id=current_user.id,
                post_id=post_id,
                comment=form.comment.data,
                date=dt.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            session.add(new_comment)
            session.commit()
            form.comment.data = ""
            session.refresh(post)

        # Säkerställ att comments alltid är en lista
        comments = post.comments if post.comments else []
        for comment in comments:
            _ = comment.author
            _ = comment.post
        return render_template("post.html", post=post, comments=comments, form=form)

    return render_template("post.html", post=post, comments=comments, form=form)



# Redigera blogginlägg
@app.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    form = BlogForm()
    with Session() as session:
        post = session.get(Blog, post_id)
        if not post:
            flash("Inlägget hittades inte")
            return redirect(url_for("blog"))

        if form.validate_on_submit():
            post.title = form.title.data
            post.subject = form.subject.data
            post.body = form.body.data
            post.image = form.image.data
            session.commit()
            return redirect(url_for("blog_post", post_id=post.id))

        # Populate form with existing data
        form.title.data = post.title
        form.subject.data = post.subject
        form.body.data = post.body
        form.image.data = post.image
        form.submit.label.text = "Spara"

    return render_template(
        "form-page.html",
        input_video="../../static/videos/edit.mp4",
        input_text="Redigera blogg-inlägg",
        form=form
    )





# Radera blogginlägg
@app.route("/blog/<int:post_id>/delete", methods=["GET"])
@admin_only
def delete_post(post_id):
    with Session() as session:
        post = session.get(Blog, post_id)
        if not post:
            return redirect(url_for("blog"))
        session.delete(post)
        session.commit()
        return redirect(url_for("blog"))








# Skapa blogginlägg
@app.route("/blog/add", methods=["GET", "POST"])
@login_required
def add():
    form = BlogForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.get(User, current_user.id)
            new_post = Blog(
                title=form.title.data,
                subject=form.subject.data,
                body=form.body.data,
                image=form.image.data,
                date=dt.now().strftime("%Y-%m-%d %H:%M:%S"),
                author=user
            )
            session.add(new_post)
            session.commit()
            return redirect(url_for("blog"))

    return render_template(
            "form-page.html",
            input_video="../static/videos/add.mp4",
            input_text="Skapa nytt blogg-inlägg",
            form=form
        )






# Ta bort kommentar inlägg från blogginlägg
@app.route("/comment/<int:comment_id>", methods=["POST","GET"])
@admin_or_creator_only
def delete_comment(comment_id):
    with Session() as session:

        comment = session.execute(
            select(Comment).where(Comment.id == comment_id)
        ).scalar_one_or_none()

        if not comment:
            return redirect(url_for("index"))

        post_id = comment.post_id
        session.delete(comment)
        session.commit()

    return redirect(url_for("blog_post", post_id=post_id))






# Kontaktformulär – skicka mail
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_mail(form.email.data, form.message.data)
        form.email.data = ""
        form.message.data = ""
        form.submit.label.text = "Meddelande skickat"
    return render_template("form-page.html", form=form, input_video="./static/videos/contact.mp4", input_text="Kontakt")





if __name__ == "__main__":
    app.run(debug=True)