from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Integer, String, ForeignKey, Float, JSON
from sqlalchemy.orm import relationship, mapped_column

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(30), unique=True, nullable=False)
    password = mapped_column(String(200), nullable=False)

    cart = relationship("Cart", back_populates="user", uselist=False)


class Product(db.Model):
    __tablename__ = "product"
    id = mapped_column(Integer, primary_key=True)
    product = mapped_column(String(40))
    description = mapped_column(String(500))
    image = mapped_column(String())
    price = mapped_column(Integer)


class Cart(db.Model):
    __tablename__ = "cart"
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"), unique=True)

    user = relationship("User", back_populates="cart")
    items = relationship("CartItem", back_populates="cart")


class CartItem(db.Model):
    __tablename__ = "cart_item"
    id = mapped_column(Integer, primary_key=True)
    cart_id = mapped_column(ForeignKey("cart.id"))
    product_id = mapped_column(ForeignKey("product.id"))
    quantity = mapped_column(Integer, default=1)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")




class Receipt(db.Model):
    __tablename__ = "receipt"

    id = mapped_column(Integer, primary_key=True)
    order_number = mapped_column(String(20), unique=True, nullable=False)
    user_id = mapped_column(ForeignKey("user.id"), nullable=False)
    total_price = mapped_column(Float, nullable=False)
    products = mapped_column(JSON, nullable=False)

    user = relationship("User")



def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webshop.db"
    db.init_app(app)
    return db, User, Product, Cart, CartItem