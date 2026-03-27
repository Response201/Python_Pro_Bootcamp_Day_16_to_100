from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class BlogForm(FlaskForm):
    title = StringField("Titel",validators=[DataRequired(), Length(min=3, max=80)] )
    subject = StringField("Sammanfattning", validators=[DataRequired(), Length(min=10, max=150)])
    body = StringField("Inlägg", validators=[DataRequired(), Length(min=10, max=500)] )
    image = StringField("Bild URL", validators=[DataRequired(), Length(min=10, max=250)])
    submit = SubmitField(label='Lägg till')


class LoginForm(FlaskForm):

    email = StringField("E-postadress",validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField( "Lösenord",validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField("Logga in")


class RegisterForm(FlaskForm):
    name = StringField("Förnamn",validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("E-postadress",validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField("Lösenord",validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField("Registrera")




class CommentForm(FlaskForm):

    comment = CKEditorField("Kommentera", validators=[DataRequired(),Length(min=10, max=30)])
    submit = SubmitField("Skicka")



class ContactForm(FlaskForm):
    email = StringField("E-postadress",validators=[DataRequired(), Length(min=5, max=50)])
    message = StringField("Meddelande", validators=[DataRequired(message="Meddelande krävs"),Length(min=10, max=2000, message="Meddelandet måste vara mellan 10 och 2000 tecken")])

    submit = SubmitField("Skicka")