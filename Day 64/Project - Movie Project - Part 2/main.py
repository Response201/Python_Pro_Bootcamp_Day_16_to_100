import os
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import select
from forms import MovieForm_update, MovieForm_search
from functions import get_data
from database import database
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)
db, Movie = database(app)



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




# Ta bort en film
@app.route("/delete/<movie_id>")
def delete(movie_id):

    movie = db.session.execute(select(Movie).where(Movie.id==movie_id)).scalar()
    if movie:
                db.session.delete(movie)
                db.session.commit()
    return  redirect("/")





# Hämta filmer från API baserat på titel(och params)
@app.route("/search", methods=["GET", "POST"])
def search():
    form = MovieForm_search()
    url = "search/movie"
    params = {
        "query": form.title.data,
        "original_language":'en',
        "page": 1,
        "include_adult": False
    }

    # Hämta filmer
    data = get_data(url, params)
    list = data["results"]

    if form.validate_on_submit():
        print(form.title.data)

        if list:
            return render_template("select.html", movie_list=list )

        else:
            form.title.errors.append("Movie not found")

    return render_template("add.html", form=form)





# Lägg till vald film i databasen
@app.route("/add/<movie_id>")
def add(movie_id):

    # Hämta filmdata från API
    url = f"movie/{movie_id}"
    data = get_data(url)

    new_title = data["title"]
    new_year = data["release_date"].split("-")[0] if data["release_date"] else "Unkown"

    new = db.session.execute(db.select(Movie).where(Movie.title == new_title)).scalar()
    if not new:
       new_movie = Movie(
           title=new_title,
           year=new_year,
           description= data["overview"],
           rating=0,
           ranking=10,
           review="",
           img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
       )
       db.session.add(new_movie)
       db.session.commit()
       return redirect(f"/edit/{new_movie.id}")


    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)
