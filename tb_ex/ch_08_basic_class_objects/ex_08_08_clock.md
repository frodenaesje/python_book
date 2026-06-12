---
title: "Clock"
id: "ex_08_08_clock"
tags: ["class", "property", "validation", "__str__", "cascade", "leapyear"]
difficulty: "medium"
prerequisites: ["class", "@property", "setter", "__str__", "if-elif-else"]
learning_outcomes:
  - "Implement a class with multiple properties and validation"
  - "Use cascading method calls (inc_sec -> inc_min -> inc_hour)"
  - "Handle month lengths and leap year logic"
  - "Understand why __init__ sets attributes directly rather than via property"
---

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

---
## Instructor notes

**Learning objectives covered:** property, validation, cascading methods,
calendar logic, leap year

**Why the start file is pre-built:** The Clock class is complex enough that
building it from scratch would make the exercise about boilerplate rather
than the interesting parts. The start file lets students focus on the three
methods that require real calendar reasoning - month lengths, leap years, and
cascade behaviour.

**Why __init__ sets _attr directly:** The month setter revalidates the day
when month changes. If __init__ used property setters, the order of
assignment would matter - day might be validated against the wrong month.
Setting private attributes directly avoids this initialization ordering problem.
Worth discussing explicitly.

**Chapter 9 connection:** Students will write unit tests for these three
methods in ex_09_04. Implementing them here first means they understand
the code they are testing.
