---
title: "Recursive Decimal to Binary"
id: "ex_14_08_decimal_to_binary"
tags: ["recursion", "binary", "integer division", "modulo", "linear recursion"]
difficulty: "easy"
prerequisites: ["recursion", "base case", "modulo", "integer division"]
learning_outcomes:
  - "Convert a number to binary using recursion instead of a loop"
  - "Understand how recursive results are assembled on the way back up"
  - "Connect to the iterative version from chapter 3"
---

# Recursive Decimal to Binary

## Exercise

In chapter 3 you converted a decimal number to binary using a loop
and modulo. Now solve the same problem recursively.

The key insight: the binary representation of `n` is the binary
representation of `n // 2` followed by the bit `n % 2`.

Write `to_binary(n: int) -> str` that returns the binary string for
a non-negative integer.

Base cases:
- `to_binary(0) = "0"`
- `to_binary(1) = "1"`

Recursive step: `to_binary(n) = to_binary(n // 2) + str(n % 2)`

### Part 2

Generalise to `to_base(n, base)` that converts `n` to any base from
2 to 16. For bases above 9, use letters A-F for digits 10-15.

## Example run

```
to_binary(0)    = "0"
to_binary(1)    = "1"
to_binary(10)   = "1010"
to_binary(42)   = "101010"
to_binary(255)  = "11111111"

Verify: int("101010", 2) = 42

to_base(42, 2)   = "101010"
to_base(42, 8)   = "52"
to_base(42, 16)  = "2A"
to_base(255, 16) = "FF"
```

## Topics

- Result assembled from recursive call + current bit
- Connection to ch 3 iterative version
- Base generalisation with digit lookup

---
## Instructor notes

**Learning objectives covered:** linear recursion, result assembly on
the way up, connection to ch 3

**Why the result builds on the way back:** The loop version builds the
string by prepending digits. The recursive version builds it naturally:
the deepest call returns the most significant bit, and each return adds
the next bit. No reversal needed.

**Part 2 digit lookup:**
```python
DIGITS = "0123456789ABCDEF"
def to_base(n, base):
    if n < base:
        return DIGITS[n]
    return to_base(n // base, base) + DIGITS[n % base]
```
