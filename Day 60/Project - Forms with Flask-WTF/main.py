from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


# Inloggning
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password',  validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
# nyckel för flask och wtforms
app.config['SECRET_KEY'] = 'hemlig-nyckel'
# Aktivera bootstrap
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')



@app.route("/login", methods=["GET", "POST"])
def login():

        form = LoginForm()

        if form.validate_on_submit():

            # Kontrollera inloggningsuppgifter
            if form.email.data == "admin@email.com" and form.password.data == "12345678":
                return redirect('/success')
            else:
                return redirect('/denied')

        return render_template('login.html', form=form)


@app.route("/success")
def success():

    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")



if __name__ == '__main__':
    app.run(debug=True)
