# file: sc_08_10_overload_getitem.py
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __getitem__(self, key):
        return self.cart[key]

order = Order(['Soap', 'Apple', 'Deodorant'], 'Hansen')

print(order[0])       # Soap
print(order[-1])      # Deodorant
print(order[0:2])     # ['Soap', 'Apple']
