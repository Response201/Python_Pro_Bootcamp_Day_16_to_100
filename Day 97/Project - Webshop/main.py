import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager,  current_user
from dotenv import load_dotenv
from functions.cart import count_cart
from functions.product import get_products
from database import   connect_db
from models import User,Cart, Product
from cart_routes import cart_end
from product_routes import product_end
from receipt_routes import receipt_end
from user_routes import user_end
load_dotenv()



def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    connect_db(app)
    Bootstrap5(app)



    # routes
    app.register_blueprint(cart_end)
    app.register_blueprint(product_end)
    app.register_blueprint(user_end)
    app.register_blueprint(receipt_end)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user_end.signin"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    @app.route("/", methods=["GET", "POST"])
    def home():
        sort_field = request.args.get("sort_field", "price")
        sort_dir = request.args.get("sort_dir", "asc")

        if request.method == "POST":
            sort_field = request.form.get("sort_field") or request.form.get("current_sort_field") or sort_field
            sort_dir = request.form.get("sort_dir") or request.form.get("current_sort_dir") or sort_dir

        user_id = current_user.id if current_user.is_authenticated else None

        return render_template(
            "index.html",
            products=get_products(Product, sort_field, sort_dir),
            cart_count=count_cart(Cart, user_id),
            user=current_user.is_authenticated,
            username = current_user.username if current_user.is_authenticated else "",
            show_link_btn=True,
            sort_field=sort_field,
            sort_dir=sort_dir
        )



    @app.errorhandler(404)
    def page_not_found(error):
        user_id = current_user.id if current_user.is_authenticated else None
        return render_template("404.html", cart_count=count_cart(Cart, user_id),
            user=current_user.is_authenticated,), 404


    return app


app = create_app()

def handler(request):
    return app(request.environ, lambda *args: None)

application = app