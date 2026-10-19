# Countdown - Iterator and Generator

## Exercise

Write a countdown in two ways. Assume `start` is an integer.
For a positive start, produce `start, start - 1, ..., 1`. Never produce zero.
For a start of zero or less, produce no values.

1. Implement `Countdown(start)` as an iterator class with `__iter__()`
   returning itself and `__next__()` returning the next number.
   Signal the end with `StopIteration`. Once exhausted, it must stay exhausted.
2. Implement `countdown(start)` as a generator function using `yield`.
   Do not build a list or explicitly raise `StopIteration` in the generator.
3. For each version, create a countdown from 3, retrieve one number with
   `next()`, then print the remaining numbers with `list()`.
   Print `list()` of the same object again to demonstrate exhaustion.
4. Use a fresh class instance and a fresh generator in separate `for` loops.
   Both should print `3 2 1`.
5. Show that both versions produce empty lists for starts of 0 and -2.
6. Explain which state the class stores explicitly, and which methods and
   execution state Python supplies for the generator.

Do not reset the counter in `__iter__()`. A fresh traversal requires a fresh
iterator or a fresh call to the generator function.

The `list()` constructor consumes an iterator: it repeatedly requests the next
value until `StopIteration` signals that no values remain. After `next()` has
retrieved `3`, the first `list()` call consumes the remaining values, `2` and `1`,
and stores them in a new list. The iterator is now exhausted. Calling `list()`
on that same iterator again produces `[]`, because it has no values left and
does not restart. The same applies to the generator object: `list()` resumes
it until the generator function ends, leaving it exhausted.

## Example run

```text
Iterator first: 3
Iterator remaining: [2, 1]
Iterator exhausted: []
Generator first: 3
Generator remaining: [2, 1]
Generator exhausted: []
Fresh iterator: 3 2 1
Fresh generator: 3 2 1
Zero: [] []
Negative: [] []
```

## Hints

- Check whether the countdown is finished before returning a value.
- In the generator, execution resumes after the previous `yield`.

## Topics

- The iterator protocol
- Explicit state versus a suspended generator function
- Exhaustion and fresh instances

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Countdown iterator | Implements the iterator protocol and produces integers from start down to 1 without restarting. | 40 |
| Countdown generator | Uses yield to produce the same sequence without building a list and ends normally. | 35 |
| Demonstration and comparison | Shows partial consumption, exhaustion, fresh instances, and empty cases, and explains the state handled by Python. | 25 |
| **Total** | | **100%** |
