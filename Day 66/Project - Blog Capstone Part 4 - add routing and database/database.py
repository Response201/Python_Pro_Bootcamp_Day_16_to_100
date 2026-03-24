from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float,select

def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blogs-collection.db"
    db = SQLAlchemy(app)


    class Blog(db.Model):
        __tablename__ = "posts"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        body: Mapped[str] = mapped_column(String(1000), unique=True)
        title: Mapped[str] = mapped_column(String(250), unique=True)
        subject: Mapped[str] = mapped_column(String(1000), nullable=False)
        image: Mapped[str] = mapped_column(String(1000), nullable=False)
        date:Mapped[str] = mapped_column(String(250),  nullable=False)


    with app.app_context():
        db.create_all()


    return db, Blog



