---
title: "Decimal to Binary and Hex"
id: "ex_03_02_decimal_to_base"
tags: ["binary", "hexadecimal", "modulo", "integer division", "bin", "hex"]
difficulty: "medium"
prerequisites: ["int", "input", "modulo (%)", "integer division (//)"]
learning_outcomes:
  - "Convert a decimal number to binary using % and //"
  - "Convert a decimal number to hexadecimal using % and //"
  - "Use bin() and hex() to verify the result"
  - "Understand the repeated division algorithm"
---

# Decimal to Binary and Hex

## Exercise

### Part 1

Write a program that reads a positive integer from the user and converts
it to binary **without** using `bin()`. Use only `%` and `//` as shown
in the chapter.

Verify your result by also printing `bin(number)`.

### Part 2

Extend the program to also convert to hexadecimal without using `hex()`.
Remember that hex digits go from 0-9 and then A-F.

Verify with `hex(number)`.

## Example run

```
Enter a positive integer: 5485
Binary (manual):   1010101101101
Binary (built-in): 0b1010101101101

Hexadecimal (manual):   156D
Hexadecimal (built-in): 0x156d
```

## Hint

For binary conversion:
- `number % 2` gives the next binary digit (rightmost first)
- `number //= 2` removes that digit
- Build the result string by prepending each new digit
- Stop when `number` becomes 0

For hexadecimal, use 16 instead of 2. For digits A-F, use
`chr(digit - 10 + ord('A'))` to convert 10-15 to 'A'-'F'.

## Topics

- Modulo (`%`) and integer division (`//`)
- String building with prepending
- The repeated division algorithm

---
## Instructor notes

**Learning objectives covered:** binary/hex conversion algorithm, % and //

**Why manual conversion matters:** Students who only use `bin()` and `hex()` never understand what those functions actually do. The manual algorithm makes the positional number system concrete.

**Common mistake:** Building the string with append instead of prepend - this gives the digits in reverse order.

**Part 2 hint for hex digits:** `"0123456789ABCDEF"[digit]` is a clean alternative to the chr() approach.
