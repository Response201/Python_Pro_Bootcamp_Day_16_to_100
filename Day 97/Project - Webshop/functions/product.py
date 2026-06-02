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