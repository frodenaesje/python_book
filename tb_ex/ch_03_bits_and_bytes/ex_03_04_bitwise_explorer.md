---
title: "Bitwise Explorer"
id: "ex_03_04_bitwise_explorer"
tags: ["bitwise", "AND", "OR", "XOR", "NOT", "shift", "bin"]
difficulty: "medium"
prerequisites: ["int", "input", "bin", "bitwise operators"]
learning_outcomes:
  - "Apply the bitwise operators &, |, ^, ~, <<, >>"
  - "Understand the effect of each operator on the binary representation"
  - "Connect the abstract operator to the concrete bit pattern"
---

# Bitwise Explorer

## Exercise

Write a program that reads two positive integers `a` and `b` from the user
and displays the result of all bitwise operations, showing the binary
representation for each result.

The output should show: `&` (AND), `|` (OR), `^` (XOR), `~a` (NOT),
`a << 1` (left shift by 1), and `a >> 1` (right shift by 1).

## Example run

```
Enter integer a: 12
Enter integer b: 10

a        = 12  (0b1100)
b        = 10  (0b1010)

a & b    =  8  (0b1000)   AND:   only bits set in BOTH
a | b    = 14  (0b1110)   OR:    bits set in EITHER
a ^ b    =  6  (0b0110)   XOR:   bits set in ONE but not BOTH
~a       = -13 (-0b1101)  NOT:   flips all bits (two's complement)
a << 1   = 24  (0b11000)  LEFT:  shift bits left (multiply by 2)
a >> 1   =  6  (0b110)    RIGHT: shift bits right (divide by 2)
```

## Topics

- Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`
- Binary representation with `bin()`
- Two's complement (why `~12` gives `-13`)

---
## Instructor notes

**Learning objectives covered:** all bitwise operators, two's complement intuition

**The NOT result:** `~a` gives a negative number because Python uses two's complement for negative integers. `~12 = -13` because `~n = -(n+1)` always. This is a good opportunity to revisit the two's complement section.

**Discussion:** Left shift by 1 doubles the number, right shift halves it (integer division). Ask students: what does left shift by 3 do? (Multiplies by 8 = 2³.) This is how CPUs do fast multiplication by powers of 2.
