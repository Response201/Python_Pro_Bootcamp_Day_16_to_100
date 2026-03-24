from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email


class BlogForm(FlaskForm):
    title = StringField(
        "Titel",
        validators=[DataRequired(), Length(min=3, max=250)]

    )

    subject = StringField(
        "Sammanfattning",
        validators=[DataRequired(), Length(min=10, max=1000)]
    )

    body = StringField(
        "Inlägg",
        validators=[DataRequired(), Length(min=10, max=1000)]
    )

    image = StringField(
        "Bild URL",
        validators=[DataRequired(), Length(min=10, max=250)]
    )

    submit = SubmitField(label='Lägg till')






class ContactForm(FlaskForm):
    email = StringField(
        "E-post",
        validators=[
            DataRequired(message="E-post krävs"), Email(message="Ange en giltig e-postadress"), Length(max=250)
        ]
    )

    message = TextAreaField(
        "Meddelande",
        validators=[
            DataRequired(message="Meddelande krävs"),Length(min=10, max=2000, message="Meddelandet måste vara mellan 10 och 2000 tecken")
        ]
    )

    submit = SubmitField("Skicka")