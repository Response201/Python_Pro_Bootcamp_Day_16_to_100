from flask import Blueprint, render_template
from flask_login import current_user
from functions.cart import count_cart
from functions.product import get_product
from database import  Cart, Product

product_end = Blueprint("product", __name__)

@product_end.route("/product/<int:product_id>", methods=["GET","POST"])
def product(product_id):
    user_id = current_user.id if current_user.is_authenticated else None

    return render_template(
        "product.html",
        product=get_product(Product, product_id),
        cart_count=count_cart(Cart, user_id),
        user=current_user.is_authenticated,
        show_link_btn=False
    )
