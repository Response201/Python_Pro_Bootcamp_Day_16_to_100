

def seed_database(db, Product, Cart, CartItem):


    if not db.session.query(Product).first():

        db.session.add_all([
            Product(product="Laptop", price=12000),
            Product(product="Mus", price=299),
            Product(product="Tangentbord", price=799),
        ])
        db.session.commit()

    cart = db.session.query(Cart).first()



    if not cart:
        cart = Cart()
        db.session.add(cart)
        db.session.commit()

        laptop = db.session.query(Product).filter_by(product="Laptop").first()
        mouse = db.session.query(Product).filter_by(product="Mus").first()

        db.session.add_all([
            CartItem(cart_id=cart.id, product_id=laptop.id, quantity=1),
            CartItem(cart_id=cart.id, product_id=mouse.id, quantity=2),
        ])

        db.session.commit()