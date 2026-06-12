---
title: "Chained Decorators"
id: "ex_13_08_chained_decorators"
tags: ["decorator", "chained decorators", "stacking", "order"]
difficulty: "medium"
prerequisites: ["decorator", "wrapper", "*args", "**kwargs"]
learning_outcomes:
  - "Understand that stacked decorators are applied from bottom to top"
  - "Observe how the order of decorators changes the output"
  - "Import and reuse decorators from other modules"
---

# Chained Decorators

## Exercise

When two decorators are stacked, they are applied from bottom to top.
Import the `timer` decorator from `ex_13_04_timing_decorator` and the
`log_call` decorator from `ex_13_05_logging_decorator`.

Apply both to the same function in two different orders and observe
the difference in output. Add a comment for each case explaining which
decorator is the outermost wrapper.

```python
# Order 1: timer wraps log_call
@timer
@log_call
def compute(n):
    return sum(range(n))

# Order 2: log_call wraps timer
@log_call
@timer
def compute2(n):
    return sum(range(n))
```

## Example run

```
# Order 1 output - timer sees the call to log_call's wrapper:
CALL  wrapper(1000000)
RETURN 499999500000
compute() took 12.30 ms

# Order 2 output - log_call sees the call to timer's wrapper:
compute2() took 11.98 ms
CALL  wrapper(1000000)
RETURN 499999500000
```

## Topics

- Stacked decorators: `@A` then `@B` means `A(B(func))`
- The outermost decorator controls what is printed first
- Decorators can be imported and reused like any function

---
## Instructor notes

**Learning objectives covered:** decorator stacking, application order,
import and reuse

**The order rule:** With `@A` above `@B`:
```python
compute = A(B(compute))
```
A is applied last (outermost), B is applied first (innermost).
When `compute(n)` is called, A's wrapper runs first.

**Why the function name shows as "wrapper":** Neither decorator preserves
`__name__`. Adding `@functools.wraps(func)` to wrapper in each decorator
fixes this and is good practice to mention.

**Connection to exercise 13.04 and 13.05:** This exercise deliberately
depends on the previous two. Students see that decorators are reusable
across any function - including other decorators' wrappers.
