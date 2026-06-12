# file: ex_09_04_clock_tests_start.py
# Copy clock.py from tb_sc/ch_08/ to this folder and implement
# the three missing methods before running these tests.

import unittest
from ex_08_08_clock import Clock


class TestClock(unittest.TestCase):

    # --- inc_day ---

    def test_inc_day_normal(self):
        # TODO: a normal day increment (not end of month)
        pass

    def test_inc_day_end_of_month_31(self):
        # TODO: last day of a 31-day month rolls to day 1 of next month
        pass

    def test_inc_day_end_of_month_30(self):
        # TODO: last day of a 30-day month rolls over
        pass

    def test_inc_day_february_no_leap(self):
        # TODO: Feb 28 in non-leap year should go to March 1
        pass

    def test_inc_day_february_leap(self):
        # TODO: Feb 28 in a leap year should go to Feb 29 (not March!)
        # AND: Feb 29 in a leap year should go to March 1
        pass

    # --- inc_month ---

    def test_inc_month_normal(self):
        # TODO: a normal month increment
        pass

    def test_inc_month_end_of_year(self):
        # TODO: December rolls to January of next year
        pass

    # --- inc_year ---

    def test_inc_year(self):
        # TODO: year increments by 1
        pass

    # --- cascade ---

    def test_cascade_to_new_year(self):
        # TODO: Clock(2023, 12, 31, 23, 59, 59) after one inc_sec()
        # should give year=2024, month=1, day=1, hour=0, minute=0, sec=0
        pass


if __name__ == '__main__':
    unittest.main()
