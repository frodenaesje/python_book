# Comparing Floats

## Exercise

Write a program that:

- Reads two numbers and an expected sum, all as `float`
- Computes the sum of the two numbers
- Prints the sum, then reports whether it equals the
  expected value in two ways: with `==`, and with
  `math.isclose()`

Run it with `0.1`, `0.2` and `0.3` and look closely at the
two answers.

## Example run

```
Enter the first number: 0.1
Enter the second number: 0.2
Enter the expected sum: 0.3
0.1 + 0.2 = 0.30000000000000004
Using ==:            False
Using math.isclose:  True
```

## Topics

- Floats are stored in binary and are not always exact
- `==` reports the tiny difference as "not equal"
- `math.isclose()` asks "close enough?" instead
