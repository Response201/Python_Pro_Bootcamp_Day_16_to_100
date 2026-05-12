from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField

class CafesForm_search(FlaskForm):

        name = StringField("Cafe name")
        location = StringField("Location")

        has_sockets = BooleanField("Sockets")
        has_toilet = BooleanField("Toilet")
        has_wifi = BooleanField("WiFi")
        can_take_calls = BooleanField("Can take calls")

        submit = SubmitField("Search")
        reset = SubmitField("Reset")



