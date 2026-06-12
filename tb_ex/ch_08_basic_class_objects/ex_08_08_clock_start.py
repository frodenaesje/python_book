# file: ex_08_08_clock_start.py
# Implement the three methods marked with pass: inc_day, inc_month, inc_year

class Clock:
    MONTHS_31 = [1, 3, 5, 7, 8, 10, 12]
    MONTHS_30 = [4, 6, 9, 11]

    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, sec=0):
        # Attributes are set directly (not via property) to avoid
        # initialization ordering problems - month must be set before
        # day can be validated against it.
        self._year  = max(0, year)
        self._month = month if 1 <= month <= 12 else 1
        max_day     = self.days_in_month(self._month, self._year)
        self._day   = day if 1 <= day <= max_day else 1
        self._hour  = hour   if 0 <= hour   < 24 else 0
        self._min   = minute if 0 <= minute < 60 else 0
        self._sec   = sec    if 0 <= sec    < 60 else 0

    # ── Increment methods ─────────────────────────────────────────────

    def inc_sec(self):
        if self._sec < 59:
            self._sec += 1
        else:
            self._sec = 0
            self.inc_min()

    def inc_min(self):
        if self._min < 59:
            self._min += 1
        else:
            self._min = 0
            self.inc_hour()

    def inc_hour(self):
        if self._hour < 23:
            self._hour += 1
        else:
            self._hour = 0
            self.inc_day()

    def inc_day(self):
        # TODO: increment day, rolling over to next month if needed
        # Hint: use days_in_month(self._month, self._year) for the last day
        pass

    def inc_month(self):
        # TODO: increment month, rolling over to next year if needed
        pass

    def inc_year(self):
        # TODO: increment year by 1
        pass

    # ── Properties ────────────────────────────────────────────────────

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = max(0, value)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value if 1 <= value <= 12 else 1
        max_day = self.days_in_month(self._month, self._year)
        if self._day > max_day:
            self._day = 1

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        max_day = self.days_in_month(self._month, self._year)
        self._day = value if 1 <= value <= max_day else 1

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value if 0 <= value < 24 else 0

    @property
    def minute(self):
        return self._min

    @minute.setter
    def minute(self, value):
        self._min = value if 0 <= value < 60 else 0

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, value):
        self._sec = value if 0 <= value < 60 else 0

    # ── Helper methods ────────────────────────────────────────────────

    def days_in_month(self, month, year):
        if month in self.MONTHS_31:
            return 31
        elif month in self.MONTHS_30:
            return 30
        else:
            return 29 if self.is_leapyear(year) else 28

    def is_leapyear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def set_clock(self, year, month, day, hour, minute, sec):
        self.year   = year
        self.month  = month
        self.day    = day
        self.hour   = hour
        self.minute = minute
        self.sec    = sec

    def __str__(self):
        return (f'{self._year:04d}-{self._month:02d}-{self._day:02d} '
                f'{self._hour:02d}:{self._min:02d}:{self._sec:02d}')


if __name__ == '__main__':
    clock = Clock(2023, 12, 31, 23, 59, 59)
    clock.inc_sec()
    print(clock)   # Expected: 2024-01-01 00:00:00 (after you implement the three methods)
