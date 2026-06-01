

def get_cart(cart):
    current_cart = cart.query.first()

    if not current_cart:
        return None, 0

    total_price = sum(
        item.product.price * item.quantity
        for item in current_cart.items
    )

    return current_cart, total_price



def count_cart(cart):

        cart_count = cart.query.get(1)
        if not cart_count:
            return 0


        return len(cart_count.items)

