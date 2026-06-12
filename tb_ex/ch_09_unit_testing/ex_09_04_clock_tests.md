---
title: "Complete Clock and write tests"
id: "ex_09_04_clock_tests"
tags: ["unittest", "TestCase", "assertEqual", "cascade", "leapyear", "boundary values"]
difficulty: "medium"
prerequisites: ["unittest", "TestCase", "assertEqual", "Clock from ch 8"]
learning_outcomes:
  - "Implement methods in an existing class"
  - "Write tests that cover boundary values and cascade behaviour"
  - "Test leap year edge cases"
  - "Understand the relationship between implementation and tests"
---

# Complete Clock and write tests

## Exercise

In chapter 8 you worked on `ex_08_08_clock_start.py` with three methods
left incomplete: `inc_day()`, `inc_month()` and `inc_year()`.

### Part 1 - Complete the implementation

Open `ex_08_08_clock_start.py` from the chapter 8 source folder and
implement the three missing methods. Then copy your completed
`ex_08_08_clock.py` to this folder before running the tests.

**`inc_day()`**
- If the current day is less than the last day of the current month:
  increment the day
- Otherwise: set day to 1 and call `inc_month()`
- Use `days_in_month(self._month, self._year)` for the last day

**`inc_month()`**
- If the current month is less than 12: increment the month
- Otherwise: set month to 1 and call `inc_year()`

**`inc_year()`**
- Increment the year by 1

### Part 2 - Write the tests

Create `test_clock.py` and write a `TestClock` class.
Cover these scenarios:

**`inc_day()`:**
- Normal day increment
- Last day of a 31-day month (rolls to next month)
- Last day of a 30-day month
- February 28 in a non-leap year (rolls to March 1)
- February 28 in a leap year (rolls to Feb 29, not March)
- February 29 in a leap year (rolls to March 1)

**`inc_month()`:**
- Normal month increment
- December rolls to January of next year

**`inc_year()`:**
- Simple increment

**Cascade:**
- `Clock(2023, 12, 31, 23, 59, 59)` after one `inc_sec()` gives
  `2024-01-01 00:00:00`

## Example run

```
python -m unittest test_clock -v

test_cascade_to_new_year ... ok
test_inc_day_end_of_month_30 ... ok
test_inc_day_end_of_month_31 ... ok
test_inc_day_february_leap ... ok
test_inc_day_february_no_leap ... ok
test_inc_day_normal ... ok
test_inc_month_end_of_year ... ok
test_inc_month_normal ... ok
test_inc_year ... ok

Ran 9 tests in 0.001s
OK
```

## Topics

- Implementing methods that cascade
- Boundary value testing for calendar logic
- Leap year edge cases
- Testing cascade behaviour end-to-end

---
## Instructor notes

**Learning objectives covered:** implementation + testing, calendar boundaries,
cascade testing, leap year

**Why this is a capstone exercise:** Students both implement and test. They
experience the full TDD-adjacent cycle: write failing tests first (or at least
think about what should pass), implement, verify. The cascade test is
particularly satisfying - it exercises the entire inc chain in one assertion.

**Leap year cases are the hardest:** Feb 28 in a leap year should give Feb 29,
not March 1. Students who forget this case have an incomplete implementation.
Writing the test first makes the requirement explicit.
