# file: test_clock.py
# This file is a copy of sc_08_16_clock.py.
# This is done to simplify import.

import pytest
from clock import Clock


# Fixtures

@pytest.fixture
def default_clock():
    """Return a clock with default values."""
    return Clock()


# Initialization

def test_init_valid_values():
    clock = Clock(2023, 6, 15, 14, 30, 45)
    assert clock.year   == 2023
    assert clock.month  == 6
    assert clock.day    == 15
    assert clock.hour   == 14
    assert clock.minute == 30
    assert clock.sec    == 45


def test_init_default_values(default_clock):
    assert default_clock.year   == 0
    assert default_clock.month  == 1
    assert default_clock.day    == 1
    assert default_clock.hour   == 0
    assert default_clock.minute == 0
    assert default_clock.sec    == 0


def test_init_invalid_values():
    clock = Clock(-5, 13, 32, 25, 61, 61)
    assert clock.year   == 0
    assert clock.month  == 1
    assert clock.day    == 1
    assert clock.hour   == 0
    assert clock.minute == 0
    assert clock.sec    == 0


# Leap years and February

def test_february_leap_year():
    # February 29 is valid in leap years.
    clock1 = Clock(2020, 2, 29)
    assert clock1.day == 29

    # February 29 in a non-leap year is corrected to day 1.
    clock2 = Clock(2021, 2, 29)
    assert clock2.day == 1


@pytest.mark.parametrize("year, expected", [
    (2000, True),    # divisible by 400
    (2004, True),    # divisible by 4, not by 100
    (1900, False),   # divisible by 100, not by 400
    (2001, False),   # not divisible by 4
])
def test_is_leapyear(default_clock, year, expected):
    assert default_clock.is_leapyear(year) == expected


@pytest.mark.parametrize("month, year, expected_days", [
    (1, 2023, 31),   # January
    (4, 2023, 30),   # April
    (2, 2020, 29),   # February in a leap year
    (2, 2021, 28),   # February in a non-leap year
])
def test_days_in_month(default_clock, month, year, expected_days):
    assert default_clock.days_in_month(month, year) == expected_days


def test_month_change_revalidates_day():
    # January 31 -> February: day 31 is invalid.
    clock = Clock(2023, 1, 31)
    clock.month = 2
    assert clock.day == 1

    # April 30 -> May: day 30 is valid in May.
    clock = Clock(2023, 4, 30)
    clock.month = 5
    assert clock.day == 30

    # May 30 -> February: day 30 is invalid again.
    clock.month = 2
    assert clock.day == 1


# inc_sec and inc_min

def test_inc_sec():
    clock = Clock(2023, 1, 1, 0, 0, 58)
    clock.inc_sec()
    assert clock.sec == 59

    # Second rolls over to 0 and increments minute.
    clock.inc_sec()
    assert clock.sec    == 0
    assert clock.minute == 1


def test_inc_min():
    clock = Clock(2023, 1, 1, 0, 58, 0)
    clock.inc_min()
    assert clock.minute == 59

    # Minute rolls over to 0 and increments hour.
    clock.inc_min()
    assert clock.minute == 0
    assert clock.hour   == 1


def test_inc_hour():
    clock = Clock(2023, 1, 15, 22, 0, 0)
    clock.inc_hour()
    assert clock.hour == 23

    # At midnight inc_day() is called, but is not implemented yet.
    clock.inc_hour()
    assert clock.hour == 0
    assert clock.day  == 15   # unchanged: inc_day() is pass
