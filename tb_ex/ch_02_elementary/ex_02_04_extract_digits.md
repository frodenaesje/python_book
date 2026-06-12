---
title: "Extract Digits"
id: "ex_02_04_extract_digits"
tags: ["modulo", "integer division", "int"]
difficulty: "medium"
prerequisites: ["int", "input", "modulo (%)", "integer division (//)"]
learning_outcomes:
  - "Use modulo (%) to extract the last digit of a number"
  - "Use integer division (//) to remove the last digit"
  - "Combine % and // to process a number digit by digit"
---

# Extract Digits

## Exercise

Write a program that:
1. Asks the user for a **four-digit integer**
2. Extracts each digit using modulo (`%`) and integer division (`//`)
3. Prints the digits in reverse order

**Important:** Do not use loops or slicing (e.g. `str(n)[::-1]`).

## Example run

```
Enter a four-digit integer: 5628
The number in reverse order is: 8265
```

## Hint

For a number like 1234:
- Last digit: `1234 % 10 = 4`
- Remove last digit: `1234 // 10 = 123`
- Next digit: `123 % 10 = 3`
- And so on...

## Topics

- Modulo operator (`%`)
- Integer division (`//`)
- Digit extraction without loops or strings

---
## Instructor notes

**Learning objectives covered:** % and // operators, understanding positional value in integers

**Why no loops/slicing:** This exercise forces students to understand what % and // actually do to a number. Converting to string and slicing is trivial - the point is the arithmetic insight.

**Hint to students:** Apply % 10 to get the last digit, then // 10 to "shift" the number right. Repeat four times.
