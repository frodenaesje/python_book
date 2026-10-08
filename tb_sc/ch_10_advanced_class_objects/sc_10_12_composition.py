# file: sc_10_12_composition.py
class OrderLine:
    def __init__(self, product: str, quantity: int, price: float) -> None:
        self._product  = product
        self._quantity = quantity
        self._price    = price

    def line_total(self) -> float:
        return self._quantity * self._price

class Order:
    def __init__(self, order_id: str) -> None:
        self._order_id = order_id
        self._lines: list[OrderLine] = []

    def add_line(self, product: str, quantity: int, price: float) -> None:
        self._lines.append(OrderLine(product, quantity, price))

    def total(self) -> float:
        return sum(line.line_total() for line in self._lines)

order = Order("ORD-001")
order.add_line("Coffee", 2, 89.90)
order.add_line("Tea",    1, 49.90)
print(f"Total: {order.total():.2f}")   # Total: 229.70
