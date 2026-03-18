from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  select


app = Flask(__name__)



# 1 - Konfigurera databas
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)



# 2 - Skapa databasmodell
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)




# 3 - Skapa tabell i databasen
with app.app_context():
    db.create_all()



@app.route('/')
def home():

    # Hämta alla böcker sorterat efter ID
    result = db.session.execute(select(Book).order_by(Book.id))
    all_books = result.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route('/delete', methods=["POST"])
def delete():

        book_id = request.form["delete"]

        # Här hämtas en bok med ett specifikt och unikt ID.
        # Därför kan jag använda en enklare och mer lättläst syntax.

        # Hämta boken med det givna ID:t, eller None om den inte finns - bra vid mer specifika databassökningar
        # delete_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

        # Hämta första boken med det givna ID:t, eller None om den inte finns - lättläst och bra vid enkla databassökningar
        delete_book = Book.query.filter_by(id=book_id).first()

        # Kontrollerar om boken finns
        if delete_book:
            db.session.delete(delete_book)
            db.session.commit()

        return redirect("/")





@app.route('/edit/<book_id>', methods=["GET","POST"])
def edit(book_id):
        this_book = Book.query.filter_by(id=book_id).first()
        print(this_book)
        if this_book:

            if request.method == "POST":
                this_book.rating = request.form["rating"]
                db.session.commit()
                return redirect("/")

        else:
           return redirect("/404")



        return render_template("edit.html", book = this_book)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        if new_title and author and rating:

            # Kontrollera om boken redan finns
            existing_book = Book.query.filter_by(title=new_title).first()
            if existing_book:

                print("This book already exists!")

            else:

                # Lägg till ny bok i databasen
                new_book = Book(title=new_title, author=author, rating=rating)
                db.session.add(new_book)
                db.session.commit()
                return redirect("/")


    return render_template("add.html")



@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)

