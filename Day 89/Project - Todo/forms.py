from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class Create_todo(FlaskForm):

    task = StringField(
        "Task",
        validators=[ DataRequired(), Length(max=40)]
    )

    subject = StringField(
        "Subject",
        validators=[ DataRequired(),Length(max=200)]
    )

    submit = SubmitField("Add")