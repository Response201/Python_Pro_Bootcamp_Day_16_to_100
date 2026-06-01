import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from database import database
from seed_database import seed_database
from functions import  get_cart, count_cart
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)
db, Product,Cart,CartItem = database(app)


with app.app_context():
    seed_database(db, Product, Cart, CartItem)



@app.route("/", methods=["GET"])
def home():

    return render_template(
        "index.html",
        cart_count=count_cart(Cart)
    )

@app.route("/cart")
def cart():

    current_cart, total_price = get_cart(Cart)
    for item in current_cart.items:
        print(item.product.product)

    return render_template(
        "cart.html",
        cart=current_cart,
        total_price=total_price,
        cart_count=count_cart(Cart)
    )





if __name__ == '__main__':
    app.run(debug=True)