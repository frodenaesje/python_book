# file: test_sc_09_05_coverage_examples.py
import unittest
from sc_09_05_coverage_examples import (
    add, greet, is_even, is_valid, subtract
)

class TestCoverageExamples(unittest.TestCase):

    # Line coverage: tests that the line in greet() is executed.
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    # Branch coverage: tests both if and else in is_even().
    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(3))

    # Function/method coverage: tests add(), but not subtract().
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    # Condition coverage: tests is_valid() with varied truth values.
    def test_is_valid_true(self):
        self.assertTrue(is_valid(5))  # True and True

    def test_is_valid_false_low(self):
        self.assertFalse(is_valid(-1))  # False and True

    def test_is_valid_false_high(self):
        self.assertFalse(is_valid(15))  # True and False

if __name__ == "__main__":
    unittest.main()
