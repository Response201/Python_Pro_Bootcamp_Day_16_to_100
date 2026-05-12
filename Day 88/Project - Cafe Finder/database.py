from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
    db = SQLAlchemy(app)

    class Cafe(db.Model):
        __tablename__ = "cafe"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        name: Mapped[str] = mapped_column(String(250), nullable=False)
        map_url: Mapped[str] = mapped_column(String(500), nullable=False)
        img_url: Mapped[str] = mapped_column(String(500), nullable=False)
        location: Mapped[str] = mapped_column(String(250), nullable=False)
        has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
        has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
        has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
        can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
        seats: Mapped[str] = mapped_column(String(250))
        coffee_price: Mapped[str] = mapped_column(String(250))


    with app.app_context():
        db.create_all()


    return db, Cafe