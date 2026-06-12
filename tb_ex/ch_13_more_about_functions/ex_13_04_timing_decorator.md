---
title: "Timing Decorator"
id: "ex_13_04_timing_decorator"
tags: ["decorator", "wrapper", "*args", "**kwargs", "time", "@-syntax"]
difficulty: "medium"
prerequisites: ["decorator", "wrapper function", "*args", "**kwargs", "time.perf_counter"]
learning_outcomes:
  - "Write a decorator manually and apply it with the @-syntax"
  - "Use *args and **kwargs so the wrapper handles any function signature"
  - "Understand that @timer is shorthand for f = timer(f)"
---

# Timing Decorator

## Exercise

Write a decorator `@timer` that measures and prints the execution time
of any function. Use `time.perf_counter()` for timing.

The wrapper must use `*args` and `**kwargs` so it works with functions
of any signature. Print the function name and elapsed time in
milliseconds.

Apply the decorator to at least three functions with different signatures:

1. A function with no parameters (e.g. compute all primes below 100 000)
2. A function with one parameter
3. A function with two parameters

## Example run

```
find_primes() took 18.43 ms
fibonacci(35) took  4.92 ms
sort_words("banana apple cherry") took  0.01 ms
```

## Topics

- Decorator pattern: outer function takes `func`, inner `wrapper` calls it
- `@timer` as shorthand for `find_primes = timer(find_primes)`
- `*args` and `**kwargs` for arbitrary signatures
- `time.perf_counter()` for high-resolution timing

---
## Instructor notes

**Learning objectives covered:** decorator, wrapper, *args/**kwargs, @-syntax,
perf_counter

**The @-syntax equivalence:** Show students both:
```python
@timer
def find_primes(): ...
# is exactly the same as:
def find_primes(): ...
find_primes = timer(find_primes)
```

**functools.wraps:** In production code, `@functools.wraps(func)` should
be applied to wrapper to preserve `__name__` and `__doc__`. This is a
good mention without requiring it for the exercise.

**Connection to book section 13.4.2:** The book uses a timing decorator
to compare sorting algorithms. This exercise extends that pattern to any
function.
