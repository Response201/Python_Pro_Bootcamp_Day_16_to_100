import os
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import  FloatField
from wtforms.validators import DataRequired, Length, NumberRange
from database import database
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)
db, Movie = database(app)




class MovieForm_update(FlaskForm):

    review= StringField('Movie review', validators=[DataRequired(), Length(min=3, max=50, message="Review must be between 3 and 20 characters.")])
    rating = FloatField('Movie rating', validators=[NumberRange(min=0, max=10, message="Rating must be between 0 and 10")])
    submit = SubmitField('Update')






# Startsida som visar topp 10 filmer
@app.route("/")
def home():

    # Hämta topp 10 filmer sorterade på betyg
    movies = db.session.execute(select(Movie).order_by(-Movie.rating).limit(10)).scalars().all()

    # Sätt ranking för varje film
    for movie in range(len(movies)):
        movies[movie].ranking = movie+1
    db.session.commit()

    # Hämta uppdaterad lista
    movies = db.session.execute(select(Movie).order_by(-Movie.rating).limit(10)).scalars().all()

    return render_template("index.html", movies=movies)






# Redigera en films betyg och recension
@app.route("/edit/<movie_id>",  methods=["GET", "POST"])
def edit(movie_id):

    movie = db.session.execute(select(Movie).where(Movie.id==movie_id)).scalar()
    if movie:
        existing_rating = movie.rating
        existing_review = movie.review
        form = MovieForm_update()
        if request.method == "GET":
             form.review.data = existing_review
             form.rating.data = existing_rating

        if form.validate_on_submit():
                movie.rating = form.rating.data
                movie.review = form.review.data
                db.session.commit()
                return redirect("/")

        return render_template("edit.html", form=form, movie_title=movie.title )

    else:
        return redirect("/")



if __name__ == '__main__':
    app.run(debug=True)
