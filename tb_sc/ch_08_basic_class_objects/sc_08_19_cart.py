# file: sc_08_19_cart.py
from dataclasses import dataclass


@dataclass
class CartItem:
    name: str
    unit_price: float
    quantity: int = 1

    def line_total(self) -> float:
        return self.unit_price * self.quantity


class Cart:
    def __init__(self, customer: str):
        self._customer = customer
        self._items: list[CartItem] = []

    def add(
        self, name: str, unit_price: float,
        quantity: int = 1
    ) -> None:
        """Add an item or increase its quantity."""
        for item in self._items:
            if item.name == name:
                item.quantity += quantity
                return
        self._items.append(
            CartItem(name, unit_price, quantity)
        )

    @property
    def total(self) -> float:
        return sum([
            item.line_total() for item in self._items
        ])

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> CartItem:
        return self._items[index]

    def __contains__(self, name: str) -> bool:
        return name in [item.name for item in self._items]

    def __str__(self) -> str:
        lines = [f"Cart for {self._customer}:"]
        for item in self._items:
            lines.append(
                f"  {item.quantity} x {item.name:<16}"
                f"{item.line_total():>10,.2f}"
            )
        lines.append(
            f"  {'Total':<20}{self.total:>10,.2f}"
        )
        return "\n".join(lines)


if __name__ == "__main__":
    cart = Cart("Alice")
    if not cart:
        print("The cart is empty.")

    cart.add("USB-C cable", 149.00)
    cart.add("Wireless mouse", 399.50)
    cart.add("USB-C cable", 149.00, quantity=2)

    print(cart)
    print(f"Different items: {len(cart)}")
    print(f"First item: {cart[0]}")
    print(f"Mouse in cart? {'Wireless mouse' in cart}")
    print(f"Keyboard in cart? {'Keyboard' in cart}")
