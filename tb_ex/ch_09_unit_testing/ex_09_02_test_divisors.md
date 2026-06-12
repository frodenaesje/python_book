---
title: "Testing proper_divisors and is_perfect"
id: "ex_09_02_test_divisors"
tags: ["unittest", "TestCase", "assertEqual", "assertIn", "assertTrue", "assertFalse"]
difficulty: "easy"
prerequisites: ["unittest", "TestCase", "assertEqual", "assertTrue", "assertFalse"]
learning_outcomes:
  - "Test a function that returns a list"
  - "Use assertIn and assertNotIn"
  - "Use assertTrue and assertFalse for bool-returning functions"
  - "Design tests that cover known mathematical facts"
---

# Testing proper_divisors and is_perfect

## Exercise

Write unit tests for two functions from chapter 6:
- `proper_divisors()` from `ex_06_03_proper_divisors.py`
- `is_perfect()` from `ex_06_03_proper_divisors.py`

### proper_divisors tests

Write a `TestProperDivisors` class testing:

- `test_known_divisors` - check that `proper_divisors(12)` returns `[1, 2, 3, 4, 6]`
- `test_prime_has_one_divisor` - a prime number has only 1 as a proper divisor
- `test_one_has_no_divisors` - `proper_divisors(1)` returns `[]`
- `test_divisor_not_included` - the number itself is never in its own divisor list

### is_perfect tests

Write a `TestIsPerfect` class testing:

- `test_known_perfect_numbers` - 6, 28, 496 and 8128 are all perfect
- `test_not_perfect` - 1, 2, 12, 100 are not perfect
- `test_prime_not_perfect` - prime numbers are never perfect

## Example run

```
python -m unittest ex_09_02_test_divisors -v

test_divisor_not_included ... ok
test_known_divisors ... ok
test_one_has_no_divisors ... ok
test_prime_has_one_divisor ... ok
test_known_perfect_numbers ... ok
test_not_perfect ... ok
test_prime_not_perfect ... ok

Ran 7 tests in 0.002s
OK
```

## Topics

- Testing list return values
- `assertIn`, `assertNotIn`
- `assertTrue`, `assertFalse`
- Known mathematical facts as test oracles

---
## Instructor notes

**Learning objectives covered:** list testing, assertIn/assertNotIn,
assertTrue/assertFalse, mathematical oracles

**Why perfect numbers are good test data:** They are well-known and can
be verified independently. Students can look them up to confirm. The rarity
of perfect numbers (only four below 10 000) also means `is_perfect` returns
False for most inputs - important to test both directions.

**Test oracle discussion:** Where do the expected values come from? In this
case from mathematics. In real software they often come from a specification,
an existing trusted implementation, or domain knowledge. Worth discussing.
