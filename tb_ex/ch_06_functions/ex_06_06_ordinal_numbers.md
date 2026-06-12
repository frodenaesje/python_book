---
title: "Ordinal Numbers"
id: "ex_06_06_ordinal_numbers"
tags: ["function", "str", "if-elif", "modulo", "type hint"]
difficulty: "easy"
prerequisites: ["def", "return", "str", "modulo (%)", "if-elif", "type hint"]
learning_outcomes:
  - "Handle special cases before general rules"
  - "Use modulo to detect patterns in numbers"
  - "Return a string from a function"
---

# Ordinal Numbers

## Exercise

Write a function `ordinal(n: int) -> str` that takes a positive integer
and returns a string containing the ordinal representation.

The rules for English ordinals:
- Numbers ending in 11, 12, 13: always use "th" (11th, 12th, 13th)
- Numbers ending in 1 (but not 11): "st" (1st, 21st, 101st)
- Numbers ending in 2 (but not 12): "nd" (2nd, 22nd)
- Numbers ending in 3 (but not 13): "rd" (3rd, 23rd)
- All others: "th" (4th, 20th, 100th)

Write a main program that displays the ordinals for 1 through 25,
and also lets the user enter any number to see its ordinal.

## Example run

```
1st   2nd   3rd   4th   5th   6th   7th   8th   9th   10th
11th  12th  13th  14th  15th  16th  17th  18th  19th  20th
21st  22nd  23rd  24th  25th

Enter a number: 111
111th
```

## Topics

- Special-case handling (11, 12, 13)
- `%` for last digit and last two digits
- String concatenation in a function

---
## Instructor notes

**Learning objectives covered:** special cases before general rules, modulo,
string return

**The key insight:** Check `n % 100` for the 11/12/13 exceptions first,
then `n % 10` for the 1/2/3 suffixes. Getting this order wrong is the
classic mistake.

**Why this exercise:** Every programmer encounters ordinals eventually.
The 11th/12th/13th exception is a perfect example of why "check the
specific case before the general case" is a fundamental programming
principle - and it gives students a satisfying "aha" moment when they
realize why it goes wrong without the check.
