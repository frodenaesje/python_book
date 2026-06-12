---
title: "Cinema Tickets"
id: "ex_04_08_cinema"
tags: ["if-elif-else", "and", "arithmetic", "input"]
difficulty: "medium"
prerequisites: ["input", "int", "float", "if-elif-else", "and"]
learning_outcomes:
  - "Determine a price based on multiple conditions"
  - "Combine age category and time of day in a single decision"
  - "Apply a discount based on quantity"
  - "Format and present a price breakdown"
---

# Cinema Tickets

## Exercise

Write a program that calculates the price of cinema tickets based on
age and time of day.

**Age categories and base prices:**

| Category         | Age        | Price |
|-----------------|------------|-------|
| Child           | Under 12   | $8    |
| Student         | 12-25      | $12   |
| Adult           | 26-66      | $16   |
| Senior          | 67 and over| $12   |

**Evening surcharge:** Adults pay $3 extra for evening screenings
(after 5 PM). All other categories pay the same price day and evening.

**Group discount:** 3 or more tickets in one purchase: 10% off the total.

## Example run

```
Age: 35
Number of tickets: 4
Evening screening? (yes/no): yes
---
Category: Adult (evening)
Price per ticket: $19
Number of tickets: 4
Subtotal: $76.00
Group discount (10%): -$7.60
Total: $68.40
```

## Topics

- `if-elif-else` with age ranges
- Combining conditions with `and`
- Discount calculation
- Formatted output

---
## Instructor notes

**Learning objectives covered:** multi-condition branching, and operator,
discount arithmetic, formatted output

**Structure hint for students:** Determine category first, then apply
surcharge separately. This keeps the logic clean and avoids deeply nested
conditions.

**Evening input:** Accept "yes"/"no" - normalize with .strip().lower().
Compare to == "yes" to get a bool.

**Good exercise for discussing:** guard clauses (validate age > 0 first),
and the difference between computing category in one block vs. computing
price and category together.
