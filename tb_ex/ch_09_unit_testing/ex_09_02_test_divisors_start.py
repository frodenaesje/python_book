# file: ex_09_02_test_divisors_start.py
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_03_proper_divisors import proper_divisors, is_perfect


class TestProperDivisors(unittest.TestCase):

    def test_known_divisors(self):
        # TODO: assert that proper_divisors(12) == [1, 2, 3, 4, 6]
        pass

    def test_prime_has_one_divisor(self):
        # TODO: a prime (e.g. 7, 13) has only [1] as proper divisors
        pass

    def test_one_has_no_divisors(self):
        # TODO: proper_divisors(1) should return []
        pass

    def test_divisor_not_included(self):
        # TODO: the number itself should never appear in its own divisor list
        # Check this for several numbers
        pass


class TestIsPerfect(unittest.TestCase):

    def test_known_perfect_numbers(self):
        # TODO: assert that 6, 28, 496 and 8128 are all perfect
        pass

    def test_not_perfect(self):
        # TODO: assert that 1, 2, 12 and 100 are not perfect
        pass

    def test_prime_not_perfect(self):
        # TODO: prime numbers are never perfect
        # Test with a few primes: 2, 3, 5, 7, 11
        pass


if __name__ == '__main__':
    unittest.main()
