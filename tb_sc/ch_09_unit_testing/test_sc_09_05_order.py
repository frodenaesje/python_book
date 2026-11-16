# file: test_sc_09_05_order.py
import pytest
from sc_09_05_order import Order


@pytest.fixture
def order():
    # Give every test the same starting point.
    Order.reset_numbering()
    return Order("Alice")


def test_new_order_is_empty(order):
    assert len(order) == 0
    assert order.total == 0


def test_add_one_line(order):
    order.add("Coffee", 49.0)
    assert len(order) == 1
    assert order.total == 49.0


def test_total_with_decimals(order):
    order.add("Candy", 0.1, quantity=3)
    assert order.total == pytest.approx(0.3)


@pytest.mark.parametrize("quantity", [0, -1, -100])
def test_invalid_quantity_raises(order, quantity):
    with pytest.raises(ValueError):
        order.add("Coffee", 49.0, quantity=quantity)


def test_first_order_gets_number_1(order):
    assert order.order_no == 1


def test_order_numbers_increase(order):
    next_order = Order("Bob")
    assert next_order.order_no == order.order_no + 1
