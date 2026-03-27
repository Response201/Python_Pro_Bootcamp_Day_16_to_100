import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, selectinload
from database import init_db, Blog, User
from forms import ContactForm
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



# Huvudsida – visar de senaste 6 inläggen
@app.route("/", methods=["GET"])
def home():
    #url_blog = url_for("blog")
    with Session() as session:
        newest_posts = session.execute(
            select(Blog)
            .options(selectinload(Blog.author))
            .order_by(Blog.date.desc())
            .limit(6)
        ).scalars().all()
    return render_template("index.html", url_blog="url_blog", posts=newest_posts)



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