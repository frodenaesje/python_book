# Pythonic patterns – Chapter 14: Recursion

Recursion has fewer purely Pythonic patterns than most other chapters — it is more about thinking correctly than writing shorter code. But some patterns are worth knowing.

## Memoisation — dict vs. `@lru_cache`

| Manual memo | Pythonic |
|-------------|----------|
| `def fibonacci_memo(n, memo=None):`<br>`    if memo is None:`<br>`        memo = {}`<br>`    if n in memo:`<br>`        return memo[n]`<br>`    ...` | `from functools import lru_cache`<br><br>`@lru_cache(maxsize=None)`<br>`def fibonacci(n):`<br>`    if n <= 1: return n`<br>`    return fibonacci(n-1) + fibonacci(n-2)` |

`@lru_cache` from the standard library handles memoisation automatically. Cleaner and more maintainable than manual dictionary management.

## Base case — check early and return

| Beginner | Pythonic |
|----------|----------|
| `def factorial(n):`<br>`    if n > 0:`<br>`        return n * factorial(n-1)`<br>`    else:`<br>`        return 1` | `def factorial(n):`<br>`    if n == 0:`<br>`        return 1`<br>`    return n * factorial(n-1)` |

For non-negative integer inputs, the two displayed forms produce the same factorial result. Checking the base case first can make the recursive structure clearer. Neither example provides general input validation.

## Recursive traversal with generator expression

| Beginner | Pythonic |
|----------|----------|
| `total = 0`<br>`for child in path.iterdir():`<br>`    total += get_size(child)`<br>`return total` | `return sum(get_size(child) for child in path.iterdir())` |

A generator expression combined with `sum()` is concise and readable for recursive aggregation.

## Mutable default argument — the `None` pattern

| Wrong | Correct |
|-------|---------|
| `def fibonacci_memo(n, memo={}):`<br>`    # memo is reused across calls!` | `def fibonacci_memo(n, memo=None):`<br>`    if memo is None:`<br>`        memo = {}` |

Use `None` when each independent top-level call should start with a fresh dictionary. Recursive calls can share the dictionary explicitly. A mutable default persists across calls and should be used only when that shared state is intentional. See chapter 6.
