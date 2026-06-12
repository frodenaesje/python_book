---
title: "Magic Dates"
id: "ex_06_02_magic_dates"
tags: ["function", "bool", "nested loops", "return", "type hint"]
difficulty: "easy"
prerequisites: ["def", "return", "bool", "for", "range", "type hint"]
learning_outcomes:
  - "Write a function that returns a bool"
  - "Use a function inside nested loops"
  - "Understand how functions reduce code repetition"
---

# Magic Dates

## Exercise

A magic date is a date where the day multiplied by the month equals
the last two digits of the year. For example, June 10, 1960 is a magic
date because 6 * 10 = 60, which equals the last two digits of 1960.

Write a function `is_magic_date(day: int, month: int, year: int) -> bool`
that returns `True` if the date is a magic date, `False` otherwise.

Use the function in a main program that finds and displays all magic
dates in the 20th century (1900-1999).

## Example run

```
Magic dates in the 20th century:
01/01/1901
02/01/1902
03/01/1903
...
01/02/1902
02/02/1904
...
```

## Topics

- Function returning `bool`
- Nested `for` loops calling a function
- `if __name__ == "__main__"`

---
## Instructor notes

**Learning objectives covered:** bool return, function in loop, __main__

**The formula:** `day * month == year % 100`

**Note on day validity:** A full solution validates that the day exists
in the given month (e.g. February has no 30th). For simplicity, accept
any day 1-31 - the exercise is about functions and loops, not calendar logic.

**Discussion:** How many magic dates are there in the 20th century?
Ask students to count before running the program.
