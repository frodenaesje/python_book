# file: ex_09_04_clock_tests.py
import unittest
from ex_08_08_clock import Clock


class TestClock(unittest.TestCase):

    def test_inc_day_normal(self):
        clock = Clock(2023, 6, 14)
        clock.inc_day()
        self.assertEqual(clock.day, 15)
        self.assertEqual(clock.month, 6)

    def test_inc_day_end_of_month_31(self):
        clock = Clock(2023, 1, 31)
        clock.inc_day()
        self.assertEqual(clock.day,   1)
        self.assertEqual(clock.month, 2)

    def test_inc_day_end_of_month_30(self):
        clock = Clock(2023, 4, 30)
        clock.inc_day()
        self.assertEqual(clock.day,   1)
        self.assertEqual(clock.month, 5)

    def test_inc_day_february_no_leap(self):
        clock = Clock(2021, 2, 28)
        clock.inc_day()
        self.assertEqual(clock.day,   1)
        self.assertEqual(clock.month, 3)

    def test_inc_day_february_leap(self):
        # Feb 28 in leap year -> Feb 29
        clock = Clock(2020, 2, 28)
        clock.inc_day()
        self.assertEqual(clock.day,   29)
        self.assertEqual(clock.month, 2)
        # Feb 29 in leap year -> March 1
        clock.inc_day()
        self.assertEqual(clock.day,   1)
        self.assertEqual(clock.month, 3)

    def test_inc_month_normal(self):
        clock = Clock(2023, 6, 15)
        clock.inc_month()
        self.assertEqual(clock.month, 7)
        self.assertEqual(clock.year,  2023)

    def test_inc_month_end_of_year(self):
        clock = Clock(2023, 12, 15)
        clock.inc_month()
        self.assertEqual(clock.month, 1)
        self.assertEqual(clock.year,  2024)

    def test_inc_year(self):
        clock = Clock(2023, 6, 15)
        clock.inc_year()
        self.assertEqual(clock.year, 2024)

    def test_cascade_to_new_year(self):
        clock = Clock(2023, 12, 31, 23, 59, 59)
        clock.inc_sec()
        self.assertEqual(clock.year,   2024)
        self.assertEqual(clock.month,  1)
        self.assertEqual(clock.day,    1)
        self.assertEqual(clock.hour,   0)
        self.assertEqual(clock.minute, 0)
        self.assertEqual(clock.sec,    0)


if __name__ == '__main__':
    unittest.main()
