# file: ex_09_03_test_password_start.py
# Replace each TODO assertion with a meaningful test.
# The unfinished tests deliberately fail.
import pytest
import sys
import os

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
