from werkzeug.security import generate_password_hash
from database import db
from models import User,Cart, Product, CartItem

def seed_database():

    if not db.session.query(Product).first():
        db.session.add_all([
            Product(
                product="Laptop",
                image="https://images.pexels.com/photos/20487289/pexels-photo-20487289.jpeg",
                price=12000,
                description="A powerful laptop with high performance, ideal for work, studies, and gaming.",
                stock_quantity = 3
            ),
            Product(
                product="Mouse",
                image="https://images.pexels.com/photos/14363329/pexels-photo-14363329.jpeg",
                price=299,
                description="An ergonomic wireless mouse with high precision and long battery life.",
                stock_quantity = 2
            ),
            Product(
                product="Keyboard",
                image="https://images.pexels.com/photos/35471659/pexels-photo-35471659.jpeg",
                price=799,
                description="A mechanical keyboard with fast response and a comfortable typing experience.",
                stock_quantity = 5
            ),
        ])
        db.session.commit()

    user = db.session.query(User).first()

    if not user:
        user = User(
            username="admin",
            password=generate_password_hash("1234"),
            role = "admin"
        )
        db.session.add(user)
        db.session.commit()

    cart = db.session.query(Cart).filter_by(user_id=user.id).first()

    if not cart:
        cart = Cart(user_id=user.id)
        db.session.add(cart)
        db.session.commit()

        laptop = db.session.query(Product).filter_by(product="Laptop").first()
        mouse = db.session.query(Product).filter_by(product="Mouse").first()

        db.session.add_all([
            CartItem(cart_id=cart.id, product_id=laptop.id, quantity=1),
            CartItem(cart_id=cart.id, product_id=mouse.id, quantity=2),
        ])

    db.session.commit()