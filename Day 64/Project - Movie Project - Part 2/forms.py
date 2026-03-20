from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import  FloatField
from wtforms.validators import DataRequired, Length, NumberRange



class MovieForm_update(FlaskForm):

    review= StringField('Movie review', validators=[DataRequired(), Length(min=3, max=50, message="Review must be between 3 and 20 characters.")])
    rating = FloatField('Movie rating', validators=[NumberRange(min=0, max=10, message="Rating must be between 0 and 10")])
    submit = SubmitField('Update')



class MovieForm_search(FlaskForm):

    title = StringField('Movie title', validators=[DataRequired(), Length(min=3, max=50, message="Review must be between 3 and 20 characters.")])
    submit = SubmitField('Search')



