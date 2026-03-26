import werkzeug
from flask import  url_for,  redirect,flash
from datetime import datetime as dt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from  functions import send_mail, create_default_posts_database
from database import database
from flask import Flask, render_template
from forms import BlogForm, ContactForm, RegisterForm,LoginForm, CommentForm
import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import  select
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
db, Blog, User, Comment = database(app)

# Flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# decorator admin
def admin_only(func):
    def wrapper(*args, **kwargs):
        post_id = kwargs.get("post_id")
        this_post = db.session.execute(select(Blog).where(Blog.id == post_id)).scalar()
        if this_post and current_user and current_user.id != this_post.author_id:
            return redirect("/")

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__  # viktigt!
    return wrapper



# decorator admin or creator
def admin_or_creator_only(func):
    def wrapper(*args, **kwargs):
        comment = kwargs.get("comment_id")

        this_comment = db.session.execute(select(Comment).where(Comment.id == comment)).scalar()
        if current_user.id != this_comment.author_id and  current_user.id != this_comment.posts.author_id:
            return redirect("/")

        return func(*args, **kwargs)



    wrapper.__name__ = func.__name__  # viktigt!
    return wrapper



# Skapa inlägg vid start
#with app.app_context():
#    create_default_posts_database(db, Blog)



# Huvudsida – visar de senaste 6 inläggen
@app.route("/", methods=["GET"])
def home():
    url_blog=url_for("blog")
    newest_posts= db.session.execute(select(Blog).order_by(Blog.date.desc()).limit(6)).scalars()
    return render_template("index.html", url_blog=url_blog, posts=newest_posts)





# Registrera användare
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = db.session.execute(select(User).where(User.email == form.email.data)).scalar()
        if existing_user:
            flash("Något gick fel")
        else:
            password = werkzeug.security.generate_password_hash(form.password.data, method='scrypt', salt_length=8)

            new_user = User(
                email = form.email.data,
                name = form.name.data,
                password = password
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Registrering lyckades")
            return redirect("/login")


    return render_template("form-page.html", form=form, input_video="./static/videos/blogpage.mp4",
        input_text=f"Skapa konto")



# Logga in Användare
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(select(User).where(User.email == form.email.data)).scalar()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("/")
            else:
                flash("Något gick fel - Prova igen")

        else:
            flash("Något gick fel - Prova igen")

    return render_template("form-page.html", form=form, input_video="./static/videos/blogpage.mp4",
        input_text=f"Logga in")


# Logga ut användare
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Användare utloggad")
    return redirect("/login")






# Bloggsida – lista alla inlägg
@app.route("/blog", methods=["GET"])
@login_required
def blog():
    blog_posts =  db.session.execute(select(Blog).where(Blog.author_id == current_user.id)).scalars().all()
    url_blog = url_for("blog")
    return render_template("blog.html",posts=blog_posts, url_blog=url_blog, input_video="./static/videos/blogpage.mp4",
        input_text=f"{current_user.name.title()}s - Blogg")





# Visa ett enskilt blogginlägg
@app.route("/blog/<int:post_id>", methods=["GET", "POST"])
def blog_post(post_id):
    form = CommentForm()
    posts = db.session.execute(select(Blog).filter_by(id=post_id)).scalar()

    if form.validate_on_submit():
        new_comment = Comment(
            author_id=current_user.id,
        post_id = post_id,
        comment = form.comment.data,
        date =  dt.now().strftime("%Y-%m-%d %H:%M:%S")

        )
        db.session.add(new_comment)
        db.session.commit()
        form.comment.data =""
        return render_template("post.html", post=posts, comments=posts.comments, form=form)



    return render_template("post.html", post=posts, comments=posts.comments, form=form)



# Redigera blogginlägg
@app.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.session.get(Blog, post_id)
    form = BlogForm(obj=post)
    form.submit.label.text = "Spara"

    if form.validate_on_submit():
        post.title = form.title.data
        post.subject = form.subject.data
        post.body = form.body.data
        post.image = form.image.data
        db.session.commit()
        return redirect(url_for("blog_post", post_id=post.id))

    return render_template("form-page.html",  input_video="../../static/videos/edit.mp4",
        input_text="Redigera blogg-inlägg", form=form)



# Radera blogginlägg
@app.route("/blog/<int:post_id>/delete", methods=["GET"])
@admin_only
def delete_post(post_id):
    post = db.session.execute(select(Blog).where(Blog.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect("/")



# Skapa blogginlägg
@app.route("/blog/add", methods=["GET", "POST"])
@login_required
def add():
    form = BlogForm()

    if form.validate_on_submit():
        new_post = Blog(
        title = form.title.data,
        subject = form.subject.data,
        body = form.body.data,
        image = form.image.data,
        date=dt.now(),
        author_id = current_user.id
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect("/")

    return render_template("form-page.html",  input_video="../static/videos/add.mp4",
        input_text="Skapa nytt blogg-inlägg", form=form)




# Ta bort kommentar inlägg från blogginlägg
@app.route("/comment/<int:comment_id>", methods=["GET", "POST"])
@admin_or_creator_only
def delete_comment(comment_id):
    comment = db.session.execute(select(Comment).where(Comment.id == comment_id)).scalar()

    if not comment:

        return redirect(f"/blog/{comment.post_id}")

    db.session.delete(comment)
    db.session.commit()
    return redirect(f"/blog/{comment.post_id}")






# Kontaktformulär – skicka mail
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_mail(form.email.data, form.message.data)
        form.email.data = ""
        form.message.data =""
        form.submit.label.text =  "Meddelande skickat"

    return render_template(
        "form-page.html",
        form=form,
        input_video="./static/videos/contact.mp4",
        input_text="Kontakt"
    )




if __name__ == "__main__":
    app.run(debug=True)