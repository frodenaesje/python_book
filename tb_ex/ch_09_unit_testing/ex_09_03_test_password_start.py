# file: ex_09_03_test_password_start.py
# Run this test file with pytest, not with VS Code's Run Python File.
# From a terminal in this folder:
# python -m pytest ex_09_03_test_password_start.py -v
#
# See Exercise 9.1 for an explanation of pytest test discovery.
# First save your completed ex_06_07_password_checker.py
# in ../ch_06_functions/.
# After saving your completed tests as ex_09_03_test_password.py, run:
# python -m pytest ex_09_03_test_password.py -v

# Replace each TODO assertion with a meaningful test.
# The unfinished tests deliberately fail.
import pytest
import sys
import os

# The function we want to test is in the Chapter 6 exercise folder.
# Python searches certain folders when importing modules.
# The following line adds that folder to Python's module search path.
# This is a practical solution for these book exercises; larger projects
# should normally be organized as packages instead.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_07_password_checker import is_good_password


def test_valid_password():
    # TODO: a password with all requirements met should return True
    assert False, "Complete this test"


def test_too_short():
    # TODO: passwords shorter than 8 chars should return False
    # Test with a few examples
    assert False, "Complete this test"


def test_missing_uppercase():
    # TODO: a password with no uppercase letter should return False
    assert False, "Complete this test"


def test_missing_lowercase():
    # TODO: a password with no lowercase letter should return False
    assert False, "Complete this test"


def test_missing_digit():
    # TODO: a password with no digit should return False
    assert False, "Complete this test"


def test_exactly_eight_chars():
    # TODO: exactly 8 characters, otherwise valid - should return True
    # This is the boundary - 8 is the minimum allowed length
    assert False, "Complete this test"


def test_seven_chars():
    # TODO: exactly 7 characters, otherwise valid - should return False
    # One character below the boundary
    assert False, "Complete this test"


@pytest.mark.parametrize("password", ["Hello123", "Secure99!", "Python3X", "Test1234"])
def test_multiple_valid_passwords(password):
    # TODO: check that this password is accepted.
    assert False, "Complete this test"
