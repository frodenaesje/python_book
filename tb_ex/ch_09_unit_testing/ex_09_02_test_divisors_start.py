# file: ex_09_02_test_divisors_start.py
# Run this test file with pytest, not with VS Code's Run Python File.
# From a terminal in this folder:
# python -m pytest ex_09_02_test_divisors_start.py -v
#
# See Exercise 9.1 for an explanation of pytest test discovery.
# First save your completed ex_06_03_proper_divisors.py
# in ../ch_06_functions/.
# After saving your completed tests as ex_09_02_test_divisors.py, run:
# python -m pytest ex_09_02_test_divisors.py -v

# Replace each TODO assertion with a meaningful test.
# The unfinished tests deliberately fail.
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
    # TODO: assert that proper_divisors(12) == [1, 2, 3, 4, 6]
    assert False, "Complete this test"


def test_prime_has_one_divisor():
    # TODO: a prime (e.g. 7, 13) has only [1] as proper divisors
    assert False, "Complete this test"


def test_one_has_no_divisors():
    # TODO: proper_divisors(1) should return []
    assert False, "Complete this test"


def test_divisor_not_included():
    # TODO: the number itself should never appear in its own divisor list
    # Check this for several numbers
    assert False, "Complete this test"


def test_known_perfect_numbers():
    # TODO: assert that 6, 28, 496 and 8128 are all perfect
    assert False, "Complete this test"


def test_not_perfect():
    # TODO: assert that 1, 2, 12 and 100 are not perfect
    assert False, "Complete this test"


def test_prime_not_perfect():
    # TODO: prime numbers are never perfect
    # Test with a few primes: 2, 3, 5, 7, 11
    assert False, "Complete this test"
