# file: test_sc_09_01_calculate.py

from sc_09_01_calculate import calculate


def test_addition():
    # Arrange + Act + Assert in one line for simple cases.
    assert calculate(2, 3, "add") == 5


def test_subtraction():
    assert calculate(5, 2, "sub") == 3


def test_illegal_operation():
    # Unknown operations should return None.
    assert calculate(1, 1, "mult") is None
