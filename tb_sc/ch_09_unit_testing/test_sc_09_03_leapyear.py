# file: test_sc_09_03_leapyear.py

import pytest
from sc_09_03_leapyear import is_leap_year


# @pytest.mark.parametrize runs the test once for each row.
@pytest.mark.parametrize("year, expected", [
    (2000, True),    # Divisible by 400
    (1900, False),   # Divisible by 100, not by 400
    (2004, True),    # Divisible by 4, not by 100
    (2001, False),   # Not divisible by 4
])
def test_is_leap_year(year, expected):
    # pytest runs all combinations and reports each one separately.
    assert is_leap_year(year) == expected
