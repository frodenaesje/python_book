---
title: "Validator Decorator"
id: "ex_13_06_validator_decorator"
tags: ["decorator", "wrapper", "*args", "ValueError", "decorator factory", "lambda"]
difficulty: "medium"
prerequisites: ["decorator", "wrapper", "*args", "ValueError", "lambda"]
learning_outcomes:
  - "Write a decorator that validates function arguments before calling the function"
  - "Raise ValueError from a decorator wrapper"
  - "Write a decorator factory that takes a condition and message as parameters"
---

# Validator Decorator

## Exercise

Write a decorator `@validate_positive` that checks all numeric arguments
before calling the function. If any argument is zero or negative, raise
a `ValueError` with a helpful message instead of calling the function.

Apply it to a function `rectangle_area(width, height)` and a function
`bmi(weight_kg, height_m)`.

## Extension

Write a more general decorator factory `@validate(condition, message)`
where the condition is a lambda that takes one argument and returns a
bool. For example:

```python
@validate(lambda x: x > 0, "All arguments must be positive")
def area(width, height):
    return width * height
```

## Example run

```
rectangle_area(5, 3)   -> 15
rectangle_area(-2, 3)  -> ValueError: All arguments must be positive.
bmi(70, 1.75)          -> 22.86
bmi(70, 0)             -> ValueError: All arguments must be positive.
```

## Topics

- Decorator that validates before calling
- Checking `isinstance(arg, (int, float))` to skip non-numeric args
- Decorator factory with lambda condition

---
## Instructor notes

**Learning objectives covered:** validation decorator, ValueError from
wrapper, decorator factory

**Checking only numeric args:**
```python
for arg in args:
    if isinstance(arg, (int, float)) and arg <= 0:
        raise ValueError("All arguments must be positive.")
```

**Decorator factory:**
```python
def validate(condition, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)) and not condition(arg):
                    raise ValueError(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```
