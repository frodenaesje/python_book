# file: test_sc_09_04_ticket_price.py
import pytest
from sc_09_04_ticket_price import ticket_price


@pytest.mark.parametrize("age, expected", [
    (0, 0.0),       # youngest possible
    (5, 0.0),       # last year for free
    (6, 80.0),      # first year with child ticket
    (17, 80.0),     # last year with child ticket
    (18, 160.0),    # first year with full price
    (66, 160.0),    # last year with full price
    (67, 80.0),     # first year with senior ticket
    (100, 80.0),
])
def test_price_at_age_limits(age, expected):
    assert ticket_price(age) == expected


def test_other_base_price():
    assert ticket_price(30, base_price=200.0) == 200.0
    assert ticket_price(10, base_price=200.0) == 100.0


def test_negative_age_raises():
    with pytest.raises(ValueError):
        ticket_price(-1)
