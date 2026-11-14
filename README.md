# Checkout test repository

Orders of $60 or more receive a $10 discount. Shipping is free when the
subtotal after discount is at least $50. Otherwise shipping costs $5.
The checkout total is the discounted subtotal plus shipping.

A $60 order must total $50. The regression changes the shipping threshold
from inclusive to exclusive, so checkout incorrectly charges $55.
