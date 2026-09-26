# Clock

## Exercise

The start file `clock.py` is available in the source code folder for this
chapter. It contains a `Clock` class with properties, validation, `__str__`,
and the increment methods `inc_sec`, `inc_min` and `inc_hour` already
implemented.

Three methods have been deliberately left incomplete:

- `inc_day()` - increment the day, rolling over to the next month if needed
- `inc_month()` - increment the month, rolling over to the next year if needed
- `inc_year()` - increment the year

### Your task

Open `clock.py` and implement the three methods marked with `pass`.

**`inc_day()`**
- If the current day is less than the last day of the current month:
  increment the day
- Otherwise: set day to 1 and call `inc_month()`
- Use `days_in_month(self._month, self._year)` to find the last day

**`inc_month()`**
- If the current month is less than 12: increment the month
- Otherwise: set month to 1 and call `inc_year()`

**`inc_year()`**
- Increment the year by 1

### Test your implementation

```python
clock = Clock(2023, 12, 31, 23, 59, 59)
clock.inc_sec()
print(clock)   # 2024-01-01 00:00:00

leap = Clock(2020, 2, 28)
leap.inc_day()
print(leap)    # 2020-02-29 00:00:00  (leap year)

no_leap = Clock(2021, 2, 28)
no_leap.inc_day()
print(no_leap) # 2021-03-01 00:00:00  (not a leap year)
```

## Example run

```
2024-01-01 00:00:00
2020-02-29 00:00:00
2021-03-01 00:00:00
```

## Topics

- Property validation
- Cascading increment methods
- Month length and leap year logic
