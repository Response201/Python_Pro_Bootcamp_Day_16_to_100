from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from functions.cart import count_cart, get_total_price
from functions.product import get_product
from forms import ProductForm
from functions.auth import admin_required
from database import db, Cart, Product
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






@product_end.route("/product/add", methods=["GET", "POST"])
@admin_required
def add_product():
    if not current_user.is_authenticated or current_user.role != "admin":
        return redirect(url_for("home"))

    if request.method == "POST":
        new_product = Product(
            product=request.form["product"],
            description=request.form["description"],
            image=request.form["image"],
            price=request.form["price"],
            stock_quantity=request.form["stock_quantity"]
        )

        db.session.add(new_product)
        db.session.commit()


        return redirect(url_for("product.product", product_id=new_product.id))
    form = ProductForm()
    return render_template(
        "product_form.html",
        product=None,
        title="Add product",
        button_text="Create product",
        total_price=get_total_price(Cart, current_user.id),
        cart_count=count_cart(Cart, current_user.id),
        user=current_user.is_authenticated,
        form=form
    )


@product_end.route("/product/<int:product_id>/edit", methods=["GET", "POST"])
@admin_required
def edit_product(product_id):


    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        product.product = request.form["product"]
        product.description = request.form["description"]
        product.image = request.form["image"]
        product.price = request.form["price"]
        product.stock_quantity = request.form["stock_quantity"]

        db.session.commit()

        return redirect(url_for("product.product", product_id=product.id))
    form = ProductForm(obj=product)
    return render_template(
        "product_form.html",
        product=product,
        title="Edit product",
        button_text="Update product" ,
        total_price=get_total_price(Cart, current_user.id),
        cart_count=count_cart(Cart, current_user.id),
        user=current_user.is_authenticated,
        form=form
    )


@product_end.route("/product/<int:product_id>/delete", methods=["GET","POST"])
@admin_required
def delete_product(product_id):

    product =  get_product(Product, product_id)
    if product:
        db.session.delete(product)
        db.session.commit()

    return redirect(url_for("home"))