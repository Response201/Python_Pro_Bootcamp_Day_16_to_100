import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(100), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


# Flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/')
def home():
    return render_template("index.html")


# Registrera ny användare
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        find_user = db.session.execute(select(User).where(User.email == request.form.get("email"))).scalar()

        # Hasha lösenord
        create_pass = werkzeug.security.generate_password_hash(request.form.get("password"), method='scrypt', salt_length=8)

        if not find_user:
            new_user = User(
                email = request.form.get("email"),
                username = request.form.get("email"),
                password = create_pass,
                name = request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful")
            return redirect("/login")
        else:
            flash("Something went wrong - Try again")


    return render_template("register.html")

# Logga in
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(select(User).where(User.email == request.form.get("email"))).scalar()
        if user:
            if check_password_hash(user.password, request.form.get("password")):
                # Loggar in användaren via Flask och startar session
                login_user(user)
                return redirect("/secrets")
            else:
                flash("Wrong password - Try again")
        else:
            flash("Something went wrong - Try again")


    return render_template("login.html")


# Skyddad sida, kräver inloggning -> @login_required
@app.route('/secrets')
@login_required
def secrets():

    return render_template("secrets.html", name=current_user.name)



# Logga ut -> kräver inloggning @login_required -> avslutar session med logout_user()
@app.route('/logout', methods= ["GET","POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)
