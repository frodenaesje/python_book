# file: ex_09_04_clock_tests.py
# Keep your completed ex_08_08_clock.py in ch_08_basic_class_objects.
# Import that Chapter 8 implementation directly; no local copy is needed.
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ch_08_basic_class_objects'))

from ex_08_08_clock import Clock


def test_inc_day_normal():
    clock = Clock(2023, 6, 14)
    clock.inc_day()
    assert clock.day == 15
    assert clock.month == 6


def test_inc_day_end_of_month_31():
    clock = Clock(2023, 1, 31)
    clock.inc_day()
    assert clock.day == 1
    assert clock.month == 2


def test_inc_day_end_of_month_30():
    clock = Clock(2023, 4, 30)
    clock.inc_day()
    assert clock.day == 1
    assert clock.month == 5


def test_inc_day_february_no_leap():
    clock = Clock(2021, 2, 28)
    clock.inc_day()
    assert clock.day == 1
    assert clock.month == 3


def test_inc_day_february_leap():
    # Feb 28 in leap year -> Feb 29
    clock = Clock(2020, 2, 28)
    clock.inc_day()
    assert clock.day == 29
    assert clock.month == 2
    # Feb 29 in leap year -> March 1
    clock.inc_day()
    assert clock.day == 1
    assert clock.month == 3


def test_inc_month_normal():
    clock = Clock(2023, 6, 15)
    clock.inc_month()
    assert clock.month == 7
    assert clock.year == 2023


def test_inc_month_end_of_year():
    clock = Clock(2023, 12, 15)
    clock.inc_month()
    assert clock.month == 1
    assert clock.year == 2024


def test_inc_year():
    clock = Clock(2023, 6, 15)
    clock.inc_year()
    assert clock.year == 2024


def test_cascade_to_new_year():
    clock = Clock(2023, 12, 31, 23, 59, 59)
    clock.inc_sec()
    assert clock.year == 2024
    assert clock.month == 1
    assert clock.day == 1
    assert clock.hour == 0
    assert clock.minute == 0
    assert clock.sec == 0
