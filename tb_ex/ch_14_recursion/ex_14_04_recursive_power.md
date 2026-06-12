---
title: "Recursive Power"
id: "ex_14_06_recursive_power"
tags: ["recursion", "power", "fast exponentiation", "memoisation", "linear recursion"]
difficulty: "easy"
prerequisites: ["recursion", "base case", "integer division", "memoisation"]
learning_outcomes:
  - "Implement a simple linear recursive function"
  - "Optimise to fast exponentiation using divide-and-conquer"
  - "Count recursive calls to understand the performance difference"
---

# Recursive Power

## Exercise

### Part 1 - Simple recursive power

Write `power(base, exp)` that computes `base ** exp` recursively without
using Python's `**` operator.

Base case: `power(base, 0) = 1`
Recursive step: `power(base, exp) = base * power(base, exp - 1)`

### Part 2 - Fast exponentiation

The simple version makes `exp` recursive calls. A smarter approach
halves the exponent at each step:

- If `exp` is even: `power(base, exp) = power(base, exp // 2) ** 2`
- If `exp` is odd:  `power(base, exp) = base * power(base, exp - 1)`

Write `fast_power(base, exp)` using this approach. Add a call counter
to both functions and compare the number of calls for large exponents.

## Example run

```
power(2, 10)       = 1024  (10 calls)
fast_power(2, 10)  = 1024  (5 calls)

power(2, 100)      calls: 100
fast_power(2, 100) calls: 8
```

## Topics

- Simple linear recursion
- Fast exponentiation: divide-and-conquer with O(log n) calls
- Counting recursive calls with a mutable counter

---
## Instructor notes

**Learning objectives covered:** linear recursion, fast exponentiation,
call counting, O(n) vs O(log n)

**Fast exponentiation:**
```python
def fast_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2)
        return half * half   # compute once, square - not two recursive calls
    return base * fast_power(base, exp - 1)
```
The key insight: `half * half` uses the result of ONE recursive call
twice, rather than making two separate calls. This is what makes it O(log n).

**Call counting with a list:**
```python
calls = [0]
def fast_power(base, exp):
    calls[0] += 1
    ...
```
