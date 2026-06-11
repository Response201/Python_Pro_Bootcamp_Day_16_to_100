from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from flask_login import login_required, current_user
from functions.cart import get_cart, count_cart, add_to_cart, get_total_price, remove_from_cart, delete_from_cart, \
    user_cart, delete_user_cart
from functions.product import get_product
from database import db, Cart, Product, CartItem
import os
import stripe
from dotenv import load_dotenv
load_dotenv()

client = stripe.StripeClient(os.getenv("SECRET_STRIPE"))
stripe.api_key = os.getenv("SECRET_STRIPE")

cart_end = Blueprint("cart", __name__)


@cart_end.get("/cart")
@login_required
def cart_view():
    return render_template(
        "cart.html",
        cart=get_cart(Cart, current_user.id),
        total_price=get_total_price(Cart, current_user.id),
        cart_count=count_cart(Cart, current_user.id),
        user=current_user.is_authenticated
    )


@cart_end.post("/add/<int:product_id>")
@login_required
def add(product_id):

    sort_field = request.form.get("sort_field") or request.form.get("current_sort_field")
    sort_dir = request.form.get("sort_dir") or request.form.get("current_sort_dir")

    cart = user_cart(db, cart=Cart, user_id=current_user.id)

    product = get_product(Product, product_id)

    add_to_cart(
        db,
        cart=cart,
        product=product,
        cart_item=CartItem,
        quantity=int(request.form.get("quantity", 1))
    )

    base = request.form.get("this_path", "/").split("?")[0]

    return redirect(f"{base}?sort_field={sort_field}&sort_dir={sort_dir}")

@cart_end.post("/remove/<int:product_id>")
@login_required
def remove(product_id):
    product = get_product(Product, product_id)

    remove_from_cart(
        db,
        cart=get_cart(Cart, current_user.id),
        product=product,
        cart_item=CartItem
    )

    return redirect(request.form.get("this_path", "/"))


@cart_end.post("/delete/<int:product_id>")
@login_required
def delete(product_id):
    product = get_product(Product, product_id)

    delete_from_cart(
        db,
        cart=get_cart(Cart, current_user.id),
        product=product,
        cart_item=CartItem
    )

    return redirect(request.form.get("this_path", "/"))



@cart_end.route("/checkout",methods=["POST"])
@login_required
def check_out():

    line_items = []
    cart = get_cart(Cart, current_user.id)

    for item in cart.items:
        line_items.append({
            "price_data": {
                "currency": "USD",
                "product_data": {
                    "name": item.product.product
                },
                "unit_amount": int(item.product.price * 100),
            },
            "quantity": item.quantity
        })

    if not cart.items:
        return "Cart is empty", 400

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=url_for("cart.payment_success", _external=True),
        cancel_url=url_for("home", _external=True),
    )

    return redirect(session.url)



@cart_end.route("/payment")
@login_required
def payment_success():
    print("BETALNING GENOMFÖRD!")

    delete_user_cart(db,cart_item=CartItem,cart=get_cart(Cart, current_user.id))

    return redirect("/")