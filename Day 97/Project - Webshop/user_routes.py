from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, Cart, User

user_end = Blueprint("user", __name__)

@user_end.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect("/register")

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect("/")

    return render_template("register.html")



@user_end.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form.get("username")
        ).first()

        if user and check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect("/")
        else:
            flash("Wrong username or password")

    return render_template("login.html")



@user_end.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


