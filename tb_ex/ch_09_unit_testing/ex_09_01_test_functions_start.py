# file: ex_09_01_test_functions_start.py
import unittest
import sys
import os

# Add ch_06 to path so we can import from it
# Adjust this path to match your local folder structure
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_01_taxi_fare import taxi_fare
from ex_06_06_ordinal_numbers import ordinal


class TestTaxiFare(unittest.TestCase):

    def test_zero_distance(self):
        # TODO: 0 km should return the base fare of $4.00
        pass

    def test_known_value(self):
        # TODO: verify a known calculated value
        # Hint: use assertAlmostEqual(result, expected, places=2)
        pass

    def test_fare_increases_with_distance(self):
        # TODO: assert that a longer distance gives a higher fare
        pass

    def test_short_distance(self):
        # TODO: 0.14 km = 140 m = exactly one 140m unit = base + $0.25
        pass


class TestOrdinal(unittest.TestCase):

    def test_first_second_third(self):
        # TODO: test 1 -> "1st", 2 -> "2nd", 3 -> "3rd"
        pass

    def test_th_suffix(self):
        # TODO: test 4 -> "4th", 5 -> "5th", 10 -> "10th", 20 -> "20th"
        pass

    def test_eleven_twelve_thirteen(self):
        # TODO: test the special cases: 11 -> "11th", 12 -> "12th", 13 -> "13th"
        # These are the tricky ones - they should NOT be 11st, 12nd, 13rd
        pass

    def test_twenty_first_etc(self):
        # TODO: test 21 -> "21st", 22 -> "22nd", 23 -> "23rd"
        # These ARE 1st/2nd/3rd endings (not special)
        pass

    def test_hundred_and_eleven(self):
        # TODO: test 111 -> "111th" (not "111st")
        pass


if __name__ == '__main__':
    unittest.main()
