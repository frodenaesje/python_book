---
title: "Function Factories with Lambda"
id: "ex_13_02_function_factories"
tags: ["lambda", "closure", "factory function", "map"]
difficulty: "easy"
prerequisites: ["lambda", "closure", "map", "list"]
learning_outcomes:
  - "Return a lambda closure from a factory function"
  - "Understand that lambda is a regular function object"
  - "Use map() with a closure as the transformation function"
---

# Function Factories with Lambda

## Exercise

Write three factory functions that each return a lambda closure.

1. `make_multiplier(n)` - returns a function that multiplies its argument by `n`
2. `make_adder(n)` - returns a function that adds `n` to its argument
3. `make_power(n)` - returns a function that raises its argument to the power `n`

Use the factories to build a small toolkit: `double`, `triple`,
`add_ten`, `square` and `cube`. Apply them to a list of numbers using
`map()` and print the results.

## Example run

```
double = make_multiplier(2)
triple = make_multiplier(3)
square = make_power(2)

print(double(5))   # 10
print(triple(4))   # 12
print(square(7))   # 49

numbers = [1, 2, 3, 4, 5]
print(list(map(double, numbers)))  # [2, 4, 6, 8, 10]
print(list(map(square, numbers)))  # [1, 4, 9, 16, 25]
```

## Topics

- `lambda n: ...` as a closure inside a factory function
- The factory function captures `n` in the lambda's closure
- `map(func, iterable)` applies a function to every element

---
## Instructor notes

**Learning objectives covered:** lambda closure, factory function, map

**Why lambda here:** The body is a single expression, so lambda is the
natural fit. A def would work equally well - the closure mechanism is
identical.

**map() preview:** map() is the functional alternative to a list
comprehension. `list(map(double, numbers))` is equivalent to
`[double(x) for x in numbers]`. Both are fine; map is worth knowing.
