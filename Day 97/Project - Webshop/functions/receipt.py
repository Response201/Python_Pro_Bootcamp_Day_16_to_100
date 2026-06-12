import time


def create_receipt(db,receipt,cart, user):
    products = []
    total = 0
    order_number = f"{user}{int(time.time() * 1000)}"

    for item in cart.items:
        products.append({
            "product": item.product.product,
            "quantity": item.quantity,
            "price": item.product.price
        })

        total += item.quantity * item.product.price

    new_receipt = receipt(
    order_number=order_number,
        user_id=user,
        total_price=total,
        products=products
    )

    db.session.add(new_receipt)
    db.session.commit()

def get_all_receipts(receipt, user):
    all_receipts = receipt.query.filter_by(user_id=user).order_by(receipt.id.desc()).all()
    return all_receipts


def get_receipt(receipt,receipt_id, user):
    receipt = receipt.query.filter_by(
        id=receipt_id,
        user_id=user
    ).first()
    return receipt