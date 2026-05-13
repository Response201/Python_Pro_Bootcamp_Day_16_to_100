from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime
from datetime import datetime


def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
    db = SQLAlchemy(app)

    class Todo(db.Model):
        __tablename__ = "todo"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        task: Mapped[str] = mapped_column(String(40), nullable=False)
        subject: Mapped[str] = mapped_column(String(200), nullable=False)
        done: Mapped[bool] = mapped_column(Boolean, nullable=False)
        date: Mapped[datetime] = mapped_column( DateTime,nullable=False)

    with app.app_context():
        db.create_all()

    return db, Todo