# file: ex_09_01_test_functions_start.py
# Replace each TODO assertion with a meaningful test.
# The unfinished tests deliberately fail.
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_01_taxi_fare import taxi_fare
from ex_06_06_ordinal_numbers import ordinal


def test_zero_distance():
    # TODO: 0 km should return the base fare of $4.00
    assert False, "Complete this test"


def test_known_value():
    # TODO: verify a known calculated value
    # Hint: compare with pytest.approx(expected, abs=0.005)
    assert False, "Complete this test"


def test_fare_increases_with_distance():
    # TODO: assert that a longer distance gives a higher fare
    assert False, "Complete this test"


def test_short_distance():
    # TODO: 0.14 km = 140 m = exactly one 140m unit = base + $0.25
    assert False, "Complete this test"


def test_first_second_third():
    # TODO: test 1 -> "1st", 2 -> "2nd", 3 -> "3rd"
    assert False, "Complete this test"


def test_th_suffix():
    # TODO: test 4 -> "4th", 5 -> "5th", 10 -> "10th", 20 -> "20th"
    assert False, "Complete this test"


def test_eleven_twelve_thirteen():
    # TODO: test the special cases: 11 -> "11th", 12 -> "12th", 13 -> "13th"
    # These are the tricky ones - they should NOT be 11st, 12nd, 13rd
    assert False, "Complete this test"


def test_twenty_first_etc():
    # TODO: test 21 -> "21st", 22 -> "22nd", 23 -> "23rd"
    # These ARE 1st/2nd/3rd endings (not special)
    assert False, "Complete this test"


def test_hundred_and_eleven():
    # TODO: test 111 -> "111th" (not "111st")
    assert False, "Complete this test"
