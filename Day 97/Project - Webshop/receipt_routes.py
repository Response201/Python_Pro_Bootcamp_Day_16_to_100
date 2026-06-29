from flask import Blueprint, render_template
from flask_login import current_user, login_required
from functions.receipt import get_all_receipts, get_receipt
from functions.cart import count_cart
from models import Cart, Receipt



receipt_end = Blueprint("receipt", __name__)

@receipt_end.route("/receipts")
@login_required
def receipts():

    return render_template(
        "receipts.html",
        receipts=get_all_receipts(receipt=Receipt, user=current_user.id),
        cart_count=count_cart(Cart, user_id=current_user.id),
        user=current_user.is_authenticated
    )


@receipt_end.route("/receipt/<int:receipt_id>")
@login_required
def receipt(receipt_id):

    return render_template(
        "receipt.html",
        receipt=get_receipt(receipt=Receipt,receipt_id=receipt_id, user=current_user.id),
        cart_count = count_cart(Cart, user_id=current_user.id),
        user = current_user.is_authenticated
    )