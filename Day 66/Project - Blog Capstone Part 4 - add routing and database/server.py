from flask import  url_for,  redirect
from datetime import datetime as dt
from  functions import send_mail, create_default_posts_database
from database import database
from flask import Flask, render_template
from forms import BlogForm, ContactForm
import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import  select
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
db, Blog = database(app)


# Skapa inlägg vid start
#with app.app_context():
#    create_default_posts_database(db, Blog)




# Huvudsida – visar de senaste 6 inläggen
@app.route("/", methods=["GET"])
def home():

    url_blog=url_for("blog")
    newest_posts= db.session.execute(select(Blog).order_by(Blog.date.desc()).limit(6)).scalars()
    return render_template("index.html", url_blog=url_blog, posts=newest_posts)





# Bloggsida – lista alla inlägg
@app.route("/blog", methods=["GET"])
def blog():
    blog_posts =  db.session.execute(select(Blog)).scalars()
    url_blog = url_for("blog")
    return render_template("blog.html",posts=blog_posts, url_blog=url_blog, input_video="./static/videos/blogpage.mp4",
        input_text="Djur som Överraskar – Saker du inte visste")






# Visa ett enskilt blogginlägg
@app.route("/blog/<int:post_id>", methods=["GET"])
def blog_post(post_id):
    post = db.session.execute( select(Blog).filter_by(id=post_id)).scalar()
    return render_template("post.html", post=post)





# Redigera blogginlägg
@app.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.get(Blog, post_id)
    form = BlogForm(obj=post)
    form.submit.label.text = "Edit"

    if form.validate_on_submit():
        post.title = form.title.data
        post.subject = form.subject.data
        post.body = form.body.data
        post.image = form.image.data
        db.session.commit()
        return redirect(url_for("blog_post", post_id=post.id))

    return render_template("make-post.html",  input_video="../../static/videos/edit.mp4",
        input_text="Redigera blogg-inlägg", form=form)






# Radera blogginlägg
@app.route("/blog/<int:post_id>/delete", methods=["GET"])
def delete_post(post_id):
    post = db.session.execute(select(Blog).where(Blog.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect("/")





# Skapa blogginlägg
@app.route("/blog/add", methods=["GET", "POST"])
def add():
    form = BlogForm()

    if form.validate_on_submit():
        new_post = Blog(
        title = form.title.data,
        subject = form.subject.data,
        body = form.body.data,
        image = form.image.data,
        date=dt.now()
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect("/")

    return render_template("make-post.html",  input_video="../static/videos/add.mp4",
        input_text="Skapa nytt blogg-inlägg", form=form)





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
        "contact.html",
        form=form,
        input_video="./static/videos/contact.mp4",
        input_text="Kontakt"
    )




if __name__ == "__main__":
    app.run(debug=True)