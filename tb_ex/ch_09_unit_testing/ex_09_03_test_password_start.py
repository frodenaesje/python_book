# file: ex_09_03_test_password_start.py
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_06_functions'))

from ex_06_07_password_checker import is_good_password


class TestIsGoodPassword(unittest.TestCase):

    def test_valid_password(self):
        # TODO: a password with all requirements met should return True
        pass

    def test_too_short(self):
        # TODO: passwords shorter than 8 chars should return False
        # Test with a few examples
        pass

    def test_missing_uppercase(self):
        # TODO: a password with no uppercase letter should return False
        pass

    def test_missing_lowercase(self):
        # TODO: a password with no lowercase letter should return False
        pass

    def test_missing_digit(self):
        # TODO: a password with no digit should return False
        pass

    def test_exactly_eight_chars(self):
        # TODO: exactly 8 characters, otherwise valid - should return True
        # This is the boundary - 8 is the minimum allowed length
        pass

    def test_seven_chars(self):
        # TODO: exactly 7 characters, otherwise valid - should return False
        # One character below the boundary
        pass

    def test_multiple_valid_passwords(self):
        # TODO: use subTest() to test several valid passwords
        # with self.subTest(pw=pw):
        #     self.assertTrue(is_good_password(pw))
        passwords = ["Hello123", "Secure99!", "Python3X", "Test1234"]
        pass


if __name__ == '__main__':
    unittest.main()
