from sqlalchemy import asc, desc


def get_products(product, sort_field="price", sort_dir="desc"):

    if sort_dir == "desc":
        return product.query.order_by(desc(sort_field)).all()
    else:
        return product.query.order_by(asc(sort_field)).all()




def get_product(product, product_id):
    product_item = product.query.get(product_id)

    if not  product_item:
        return None

    return product_item


def change_stock_quantity(db,product, product_id, action="increase", cart=None):
    product_item = product.query.get(product_id)

    if not product_item:
        return None


    if action == "increase":
        if product_item.stock_quantity > 0:
            product_item.stock_quantity -= 1
            db.session.commit()
        else:
            return None

    if action == "decrease":

                product_item.stock_quantity += 1
                db.session.commit()

    if action == "delete":
        for item in cart.items:

            if item.product_id == product_item.id:

                product_item.stock_quantity += item.quantity
                db.session.commit()

    return product_item


