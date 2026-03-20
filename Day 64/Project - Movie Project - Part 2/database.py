from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float,select


def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
    db = SQLAlchemy(app)


    class Movie(db.Model):
        __tablename__ = "movies"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        title: Mapped[str] = mapped_column(String(50), unique=True)
        year: Mapped[int] = mapped_column(Integer, nullable=False)
        description: Mapped[str] = mapped_column(String(1000), nullable=False)
        rating: Mapped[float] = mapped_column(Float, nullable=False)
        ranking: Mapped[int] = mapped_column(Integer)
        review: Mapped[str] = mapped_column(String(500))
        img_url: Mapped[str] = mapped_column(String(500), nullable=False)


    with app.app_context():
        db.create_all()


    return db, Movie