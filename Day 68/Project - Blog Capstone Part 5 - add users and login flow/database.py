from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float,select

def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blogs-collection.db"
    db = SQLAlchemy(app)


    class Comment(db.Model):
        __tablename__ = "comments"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        author_id = mapped_column(db.Integer, db.ForeignKey("users.id"))
        post_id = mapped_column(db.Integer, db.ForeignKey("posts.id"))
        comment: Mapped[str] = mapped_column(String(100), nullable=False)
        date: Mapped[str] = mapped_column(String(250), nullable=False)

        author = relationship("User", back_populates="comments")
        posts = relationship("Blog", back_populates="comments")


    class Blog(db.Model):
        __tablename__ = "posts"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        body: Mapped[str] = mapped_column(String(1000), unique=True)
        title: Mapped[str] = mapped_column(String(250), unique=True)
        subject: Mapped[str] = mapped_column(String(1000), nullable=False)
        image: Mapped[str] = mapped_column(String(1000), nullable=False)
        date:Mapped[str] = mapped_column(String(250),  nullable=False)
        author_id = mapped_column(db.Integer, db.ForeignKey("users.id"))


        author = relationship("User", back_populates="posts")
        comments = relationship("Comment", back_populates="posts")


    class User(db.Model, UserMixin):
        __tablename__ = "users"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        email: Mapped[str] =mapped_column(String(50), nullable=False, unique=True)
        name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
        password: Mapped[str] = mapped_column(String(30), nullable=False)

        posts = relationship("Blog", back_populates="author")
        comments = relationship("Comment", back_populates="author")




    with app.app_context():
        db.create_all()


    return db, Blog, User, Comment



