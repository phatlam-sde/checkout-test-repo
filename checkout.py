from pricing import discounted_subtotal
from shipping import calculate_shipping


def checkout_total(total):
    subtotal = discounted_subtotal(total)
    return subtotal + calculate_shipping(subtotal)
