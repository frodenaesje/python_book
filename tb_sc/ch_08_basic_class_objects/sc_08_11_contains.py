# file: sc_08_11_contains.py
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __getitem__(self, key):
        return self.cart[key]

    def __contains__(self, key):
        return key in self.cart

order = Order(['Soap', 'Apple', 'Deodorant'], 'Hansen')

if 'Soap' in order:
    print("Soap is in the cart")
