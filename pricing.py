def discounted_subtotal(total):
    discount = 10 if total >= 60 else 0
    return total - discount
