from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey



def database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///webshop.db"
    db = SQLAlchemy(app)

    class Product(db.Model):
        __tablename__ = "product"
        id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
        product: Mapped[str] = mapped_column(String(40), nullable=False)
        description: Mapped[str] = mapped_column(String(500), nullable=True)
        image: Mapped[str] = mapped_column(String(), nullable=False)
        price: Mapped[str] = mapped_column(Integer, nullable=False)


    class Cart(db.Model):
        __tablename__ = "cart"
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        items = relationship("CartItem", back_populates="cart")


    class CartItem(db.Model):
        __tablename__ = "cart_item"
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        cart_id: Mapped[int] = mapped_column(ForeignKey("cart.id"))
        product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
        quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
        cart = relationship("Cart", back_populates="items")
        product = relationship("Product")


    with app.app_context():
        db.create_all()

    return db, Product, Cart, CartItem

