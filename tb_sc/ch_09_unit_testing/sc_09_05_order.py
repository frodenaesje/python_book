# file: sc_09_05_order.py

class Order:
    # Shared by all orders
    _next_order_no = 1

    def __init__(self, customer: str):
        self._customer = customer
        self._lines: list[tuple[str, float, int]] = []
        self._order_no = Order._next_order_no
        Order._next_order_no += 1

    @classmethod
    def reset_numbering(cls) -> None:
        cls._next_order_no = 1

    @property
    def order_no(self) -> int:
        return self._order_no

    @property
    def total(self) -> float:
        return sum([
            price * quantity
            for _, price, quantity in self._lines
        ])

    def add(
        self, name: str, price: float, quantity: int = 1
    ) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1")
        self._lines.append((name, price, quantity))

    def __len__(self) -> int:
        return len(self._lines)
