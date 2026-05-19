# file: sc_09_03_leapyear.py

def is_leap_year(year):
    """Check whether a year is a leap year.

    Note: this version has an intentional error. year // 400 == 0
    should really be year % 400 == 0.
    """
    if ((year % 4 == 0 and year % 100 != 0)
            or (year // 400 == 0)):  # error: // instead of %
        return True
    else:
        return False
