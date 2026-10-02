# file: ex_09_04_clock_tests_start.py
# Run this test file with pytest, not with VS Code's Run Python File.
# From a terminal in this folder:
# python -m pytest ex_09_04_clock_tests_start.py -v
#
# See Exercise 9.1 for an explanation of pytest test discovery.
# After saving your completed tests as ex_09_04_clock_tests.py, run:
# python -m pytest ex_09_04_clock_tests.py -v

# Replace each TODO assertion with a meaningful test.
# The unfinished tests deliberately fail.
# SIMPLE APPROACH USED IN THE BOOK:
# Copy these completed files from ../ch_08_basic_class_objects/
# into this folder (tb_ex/ch_09_unit_testing/):
# - ex_08_08_clock.py
# The ordinary imports below then work directly.

# ALTERNATIVE:
# Instead of copying, keep the completed files in their original exercise
# folder and add it to Python's module search path. Uncomment these lines:
#
# import sys
# import os
#
# sys.path.insert(
#     0,
#     os.path.join(os.path.dirname(__file__), '..', 'ch_08_basic_class_objects')
# )

from ex_08_08_clock import Clock


def test_inc_day_normal():
    # TODO: a normal day increment (not end of month)
    assert False, "Complete this test"


def test_inc_day_end_of_month_31():
    # TODO: last day of a 31-day month rolls to day 1 of next month
    assert False, "Complete this test"


def test_inc_day_end_of_month_30():
    # TODO: last day of a 30-day month rolls over
    assert False, "Complete this test"


def test_inc_day_february_no_leap():
    # TODO: Feb 28 in non-leap year should go to March 1
    assert False, "Complete this test"


def test_inc_day_february_leap():
    # TODO: Feb 28 in a leap year should go to Feb 29 (not March!)
    # AND: Feb 29 in a leap year should go to March 1
    assert False, "Complete this test"


def test_inc_month_normal():
    # TODO: a normal month increment
    assert False, "Complete this test"


def test_inc_month_end_of_year():
    # TODO: December rolls to January of next year
    assert False, "Complete this test"


def test_inc_year():
    # TODO: year increments by 1
    assert False, "Complete this test"


def test_cascade_to_new_year():
    # TODO: Clock(2023, 12, 31, 23, 59, 59) after one inc_sec()
    # should give year=2024, month=1, day=1, hour=0, minute=0, sec=0
    assert False, "Complete this test"
