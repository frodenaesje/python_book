---
title: "Sum of Integers 1 to n"
id: "ex_02_02_sum_of_integers"
tags: ["input", "int", "formula", "f-string"]
difficulty: "easy"
prerequisites: ["input", "int", "variables", "arithmetic"]
learning_outcomes:
  - "Read an integer from the user"
  - "Apply a mathematical formula"
  - "Understand integer division (//)"
  - "Present a result with f-string"
---

# Sum of Integers 1 to n

## Exercise

Write a program that:
1. Asks the user for a positive integer `n`
2. Calculates the sum of all integers from 1 to n using the formula:
   sum = n * (n + 1) / 2
3. Displays the result

## Example run

```
Enter a positive integer n: 10
The sum of all integers from 1 to 10 is 55.
```

## Topics

- `input()` and `int()` conversion
- Mathematical formula
- Integer division (`//`) to ensure an integer result
- f-string formatting

---
## Instructor notes

**Learning objectives covered:** int conversion, arithmetic, integer division

**Hint to students:** Use `//` instead of `/` in the formula - dividing by 2 with regular division gives a float (55.0), while integer division gives a clean integer (55).
