---
title: "Dog Years"
id: "ex_04_02_dog_years"
tags: ["if-elif-else", "float", "arithmetic"]
difficulty: "easy"
prerequisites: ["input", "float", "if-elif-else"]
learning_outcomes:
  - "Write an if-elif-else chain"
  - "Apply different rules depending on a condition"
  - "Format float output"
---

# Dog Years

## Exercise

It is commonly said that one human year equals 7 dog years. However, this
simple conversion does not account for the fact that dogs reach adulthood
much faster than humans. A better model counts each of the first two human
years as 10.5 dog years, and each subsequent year as 4 dog years.

Write a program that reads a dog's age in human years and displays the
equivalent age in dog years using this improved model.

## Example run

```
Enter the dog's age in human years: 3
The dog's age in dog years is 25.0.

Enter the dog's age in human years: 1
The dog's age in dog years is 10.5.
```

## Topics

- `if-elif-else`
- Arithmetic with floats
- Different calculation rules based on input

---
## Instructor notes

**Learning objectives covered:** if-elif-else, conditional arithmetic

**The model:**
- Age <= 0: invalid
- Age == 1: 10.5 dog years
- Age == 2: 21.0 dog years
- Age > 2: 21.0 + (age - 2) * 4 dog years

**Discussion:** This is a good example of a real-world formula that requires
branching. Ask students why the simple "multiply by 7" model is wrong, and
what assumptions the improved model makes.
