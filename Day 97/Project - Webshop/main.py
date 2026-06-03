import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from functions.cart import count_cart, get_cart, add_to_cart, get_total_price, remove_from_cart, delete_from_cart
from functions.product import get_products, get_product
from database import database
from seed_database import seed_database
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)

db, Product, Cart, CartItem = database(app)

with app.app_context():
    seed_database(db, Product, Cart, CartItem)



@app.route("/", methods=["GET", "POST"])
def home():
    sort_field = request.args.get("sort_field", "price")
    sort_dir = request.args.get("sort_dir", "asc")

    if request.method == "POST":
        sort_field = request.form.get("sort_field") or request.form.get("current_sort_field") or sort_field
        sort_dir = request.form.get("sort_dir") or request.form.get("current_sort_dir") or sort_dir

    return render_template(
        "index.html",
        products=get_products(Product, sort_field=sort_field, sort_dir=sort_dir),
        show_link_btn = True,
        cart_count=count_cart(Cart),
        sort_field=sort_field,
        sort_dir=sort_dir
    )



@app.get("/cart")
def cart():
    return render_template(
        "cart.html",
        cart=get_cart(Cart),
        total_price=get_total_price(Cart),
        cart_count=count_cart(Cart)
    )



@app.post("/add/<int:product_id>")
def add(product_id):

    sort_field = request.form.get("sort_field") or request.form.get("current_sort_field")
    sort_dir = request.form.get("sort_dir") or request.form.get("current_sort_dir")


    add_to_cart(db,
                cart=get_cart(Cart),
                product=get_product(Product(), product_id),
                cart_item=CartItem,
                quantity=int(request.form["quantity"]))

    if sort_dir and sort_field:
        return redirect(
            request.form.get("this_path", "/").split("?")[0]
            + f"?sort_field={sort_field}"
            + f"&sort_dir={sort_dir}"
        )

    return redirect(request.form.get("this_path", "/"))



@app.post("/remove/<int:product_id>")
def remove(product_id):
    remove_from_cart(db,
                     cart=get_cart(Cart),
                     product=get_product(Product(), product_id),
                     cart_item=CartItem,
                           )
    return redirect(request.form.get("this_path", "/"))



@app.post("/delete/<int:product_id>")
def delete(product_id):
    delete_from_cart(db,
                     cart=get_cart(Cart),
                     product=get_product(Product(), product_id),
                     cart_item=CartItem,
                     )
    return redirect(request.form.get("this_path", "/"))



@app.route("/product/<int:product_id>",methods=["GET", "POST"] )
def product(product_id):


    return render_template(
        "product.html",
        product=get_product(Product(), product_id),
        show_link_btn=False,
        cart_count=count_cart(Cart),

    )



if __name__ == '__main__':
    app.run(debug=True)
