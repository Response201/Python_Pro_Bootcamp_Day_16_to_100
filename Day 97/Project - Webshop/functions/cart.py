def user_cart(db, cart, user_id):
    current_cart = db.session.query(cart).filter_by(user_id=user_id).first()

    if not current_cart or current_cart is None:
        current_cart = cart(user_id=user_id)
        db.session.add(current_cart)
        db.session.commit()

    return current_cart


def delete_user_cart(db,cart_item,cart):

    existing_products = cart_item.query.filter_by(cart_id=cart.id).all()

    for product in existing_products:
        db.session.delete(product)

    db.session.delete(cart)
    db.session.commit()


def get_cart(cart, user_id):

    current_cart = cart.query.filter_by(user_id=user_id).first()

    if not current_cart:
        return None

    return current_cart


def get_total_price(cart,user_id):
    current_cart = cart.query.filter_by(user_id=user_id).first()

    if not current_cart:

        return  0

    total_price = sum(
        item.product.price * item.quantity
        for item in current_cart.items
    )

    return total_price


def count_cart(cart, user_id):
    if user_id:
        item_count = 0
        cart_count = cart.query.filter_by(user_id=user_id).first()

        if not cart_count:
            return 0

        for item in cart_count.items:
            item_count += item.quantity

        return item_count


def add_to_cart(db,cart, product, cart_item, quantity):



    existing_product = cart_item.query.filter_by(cart_id=cart.id,product_id=product.id ).first()

    if existing_product:
            existing_product.quantity += quantity

    else:
        existing_product = cart_item(
            cart_id=cart.id,
            product_id=product.id,
            quantity=quantity
        )

        db.session.add(existing_product)


    db.session.commit()


def remove_from_cart(db,cart, product, cart_item):
    existing_product = cart_item.query.filter_by(cart_id=cart.id,product_id=product.id ).first()

    if existing_product:

        if existing_product.quantity >=2:
            existing_product.quantity -= 1

        else:
            db.session.delete(existing_product)


    db.session.commit()


def delete_from_cart(db,cart, product, cart_item):

    existing_product = cart_item.query.filter_by(cart_id=cart.id,product_id=product.id ).first()

    if existing_product:
            db.session.delete(existing_product)


    db.session.commit()
