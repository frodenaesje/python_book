# file: ex_09_02_test_divisors.py
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_03_proper_divisors import proper_divisors, is_perfect


class TestProperDivisors(unittest.TestCase):

    def test_known_divisors(self):
        self.assertEqual(proper_divisors(12), [1, 2, 3, 4, 6])

    def test_prime_has_one_divisor(self):
        self.assertEqual(proper_divisors(7),  [1])
        self.assertEqual(proper_divisors(13), [1])
        self.assertEqual(proper_divisors(97), [1])

    def test_one_has_no_divisors(self):
        self.assertEqual(proper_divisors(1), [])

    def test_divisor_not_included(self):
        for n in [6, 12, 28, 100]:
            self.assertNotIn(n, proper_divisors(n))


class TestIsPerfect(unittest.TestCase):

    def test_known_perfect_numbers(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))
        self.assertTrue(is_perfect(496))
        self.assertTrue(is_perfect(8128))

    def test_not_perfect(self):
        self.assertFalse(is_perfect(1))
        self.assertFalse(is_perfect(2))
        self.assertFalse(is_perfect(12))
        self.assertFalse(is_perfect(100))

    def test_prime_not_perfect(self):
        for prime in [2, 3, 5, 7, 11, 13]:
            self.assertFalse(is_perfect(prime))


if __name__ == '__main__':
    unittest.main()
