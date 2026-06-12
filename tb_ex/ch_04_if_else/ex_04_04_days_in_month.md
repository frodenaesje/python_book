---
title: "Days in a Month"
id: "ex_04_04_days_in_month"
tags: ["match-case", "str", "input"]
difficulty: "easy"
prerequisites: ["input", "str", "match-case"]
learning_outcomes:
  - "Use match-case to dispatch on string values"
  - "Normalize string input with .strip().lower()"
  - "Group multiple values in a single case branch"
---

# Days in a Month

## Exercise

Write a program that reads the name of a month from the user and displays
the number of days in that month. For February, display "28 or 29 days"
to account for leap years.

Use `match-case` in your solution. Normalize the input with `.strip().lower()`
so that "January", "january" and " january " all work.

## Example run

```
Enter month name: October
October has 31 days.

Enter month name: february
february has 28 or 29 days.

Enter month name: xyz
Unknown month.
```

## Topics

- `match-case`
- String normalization with `.strip().lower()`
- Grouping values with `|` in case branches

---
## Instructor notes

**Learning objectives covered:** match-case, string normalization, case grouping

**Key pattern:** Multiple values in one case branch using `|`:
```python
case "april" | "june" | "september" | "november":
    days = 30
```
This is cleaner than four separate branches.

**Why normalize:** Input from users often has unexpected capitalization or
whitespace. `.strip().lower()` is a standard defensive pattern worth
establishing early.
