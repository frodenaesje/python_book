---
title: "Statistics with *args"
id: "ex_06_10_args_stats"
tags: ["function", "*args", "type hint", "min", "max", "sum", "docstring"]
difficulty: "easy"
prerequisites: ["def", "return", "*args", "for", "type hint"]
learning_outcomes:
  - "Write a function that accepts a variable number of arguments with *args"
  - "Iterate over *args with a for loop"
  - "Understand when *args is more flexible than a list parameter"
---

# Statistics with *args

## Exercise

Write three functions that each accept a variable number of numeric
arguments using `*args`:

1. `total(*numbers: float) -> float` - returns the sum of all arguments
2. `average(*numbers: float) -> float` - returns the mean
3. `stats(*numbers: float) -> tuple` - returns (min, max, mean) as a tuple

Do not use the built-in `sum()`, `min()` or `max()` in the implementations
- calculate the values manually with a loop to practice iterating over `*args`.

Write a main program that calls all three functions with a few different
argument counts to demonstrate that they work with any number of values.

## Example run

```
total(1, 2, 3):          6.0
average(1, 2, 3, 4, 5):  3.0
stats(4, 7, 2, 9, 1):    min=1, max=9, mean=4.6
```

## Topics

- `*args` for variable number of arguments
- Iterating over `*args`
- Tuple return value

---
## Instructor notes

**Learning objectives covered:** *args, iteration, tuple return

**Key insight:** `*args` is a tuple inside the function. Students can
iterate over it with `for number in numbers`. The difference from a list
parameter is that the caller writes `stats(4, 7, 2, 9, 1)` instead of
`stats([4, 7, 2, 9, 1])` - more natural for variable-length calls.

**Why not use built-ins:** Using `sum()`, `min()`, `max()` would obscure
the point of the exercise. Calculating manually makes students work
through the loop explicitly.

**Extension:** Add a `*args` version of `format_list` from ex_06_05:
`format_items("apple", "banana", "cherry")` instead of passing a list.
