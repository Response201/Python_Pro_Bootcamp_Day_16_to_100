

def seed_database(db, Product, Cart, CartItem):


    if not db.session.query(Product).first():

        db.session.add_all([
            Product(product="Laptop",image="https://images.pexels.com/photos/20487289/pexels-photo-20487289.jpeg", price=12000),
            Product(product="Mus",image="https://images.pexels.com/photos/14363329/pexels-photo-14363329.jpeg", price=299),
            Product(product="Tangentbord",image="https://images.pexels.com/photos/35471659/pexels-photo-35471659.jpeg", price=799),
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