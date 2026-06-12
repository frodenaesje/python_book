---
title: "Random Password Generator"
id: "ex_06_08_random_password"
tags: ["function", "random", "chr", "ord", "while", "import", "type hint"]
difficulty: "medium"
prerequisites: ["def", "return", "random", "chr()", "ord()", "while", "import"]
learning_outcomes:
  - "Write a function with no parameters"
  - "Use random.randint() with chr() to generate random characters"
  - "Import and reuse a function from another module"
  - "Use a while loop to retry until a condition is met"
---

# Random Password Generator

## Exercise

### Part 1

Write a function `random_password() -> str` that generates a random
password with:
- A random length between 7 and 10 characters
- Each character randomly selected from ASCII positions 33 to 126

Use `chr()` and `random.randint()`.

### Part 2

Import `is_good_password` from `ex_06_07_password_checker` and use it
to generate passwords until a good one is found. Count and display
how many attempts were needed.

## Example run

```
Generated password: rK#mP9qL
Attempts needed: 3
```

## Topics

- Function with no parameters
- `chr()` and `random.randint()`
- Importing from another module
- `while` loop with counter

---
## Instructor notes

**Learning objectives covered:** no-parameter function, chr/randint,
cross-module import, while loop as retry mechanism

**Why import from ex_06_07:** This is a deliberate exercise in reuse.
Students see that `is_good_password` is a general-purpose function that
can be used from anywhere - not just from its own file.

**Expected attempts:** On average it takes around 20-50 attempts to
generate a password that meets all requirements by random chance. This
is a good discussion point - why is a truly random password hard to
generate that meets human-readable requirements?

**ASCII range 33-126:** Printable characters excluding space (32).
Worth showing students `[chr(i) for i in range(33, 127)]` to see what
the range contains.
