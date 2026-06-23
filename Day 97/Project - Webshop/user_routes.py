from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, Cart, User
from forms import AuthForm

user_end = Blueprint("user", __name__)

@user_end.route("/signup", methods=["GET", "POST"])
def signup():
    form = AuthForm()

    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect("/signup")

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect("/")

    return render_template("auth.html",
                           header_text="Sign up",
                           form=form,
                           submit_text="Sign me up",
                           link_text="Sign in",
                           link=url_for("user.signup"),
                           link_secondary = url_for('user.signin') )


@user_end.route("/signin", methods=["GET", "POST"])
def signin():
    form = AuthForm()


    if current_user.is_authenticated :
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
            form = AuthForm()

    return render_template("auth.html",
                           header_text="Sign in",
                           form=form,
                           submit_text="Let me in",
                           link_text="Create account",
                           link=url_for('user.signin'),
                           link_secondary=  url_for("user.signup"))



@user_end.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/signup")


