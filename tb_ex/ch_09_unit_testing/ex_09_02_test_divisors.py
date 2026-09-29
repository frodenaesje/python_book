# file: ex_09_02_test_divisors.py
import sys
import os

# The functions we want to test are in the Chapter 6 exercise folder.
# Python searches certain folders when importing modules.
# The following line adds that folder to Python's module search path.
# This is a practical solution for these book exercises; larger projects
# should normally be organized as packages instead.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_03_proper_divisors import proper_divisors, is_perfect


def test_known_divisors():
    assert proper_divisors(12) == [1, 2, 3, 4, 6]


def test_prime_has_one_divisor():
    assert proper_divisors(7) == [1]
    assert proper_divisors(13) == [1]
    assert proper_divisors(97) == [1]


def test_one_has_no_divisors():
    assert proper_divisors(1) == []


def test_divisor_not_included():
    for n in [6, 12, 28, 100]:
        assert n not in proper_divisors(n)


def test_known_perfect_numbers():
    assert is_perfect(6) is True
    assert is_perfect(28) is True
    assert is_perfect(496) is True
    assert is_perfect(8128) is True


def test_not_perfect():
    assert is_perfect(1) is False
    assert is_perfect(2) is False
    assert is_perfect(12) is False
    assert is_perfect(100) is False


def test_prime_not_perfect():
    for prime in [2, 3, 5, 7, 11, 13]:
        assert is_perfect(prime) is False
