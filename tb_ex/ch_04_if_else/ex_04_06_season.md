---
title: "Season from Date"
id: "ex_04_06_season"
tags: ["if-elif-else", "and", "or", "str", "int"]
difficulty: "medium"
prerequisites: ["input", "str", "int", "if-elif-else", "and", "or"]
learning_outcomes:
  - "Combine 'and' and 'or' in conditional expressions"
  - "Handle boundary conditions (dates that span two seasons)"
  - "Normalize string input"
---

# Season from Date

## Exercise

The year is divided into four seasons. We use the following start dates:

| Season | Start date     |
|--------|---------------|
| Spring | March 20      |
| Summer | June 21       |
| Autumn | September 22  |
| Winter | December 21   |

Write a program that reads a month name and a day number from the user
and displays the season that date belongs to.

Normalize the month input with `.strip().lower()`.

## Example run

```
Enter month: June
Enter day: 15
Season: Spring

Enter month: december
Enter day: 21
Season: Winter

Enter month: march
Enter day: 19
Season: Winter
```

## Topics

- Combining `and` and `or`
- Boundary date logic
- String normalization

---
## Instructor notes

**Learning objectives covered:** and/or combinations, boundary conditions

**The tricky part:** Each season spans parts of two months at the boundaries.
For example, spring starts on March 20 and ends on June 20. Students must
handle months that are fully within a season separately from the boundary months.

**Suggested approach:** For each season, check:
1. The partial start month (e.g. march and day >= 20)
2. The full middle months (april, may)
3. The partial end month (june and day < 21)

**Common mistake:** Getting the boundary conditions wrong (using > instead of
>= or vice versa). Worth testing edge cases like March 19, March 20, June 20,
June 21.
