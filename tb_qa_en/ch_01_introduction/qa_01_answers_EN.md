# Chapter 1 – Answer Key: Review Questions

## Understanding

**1. "Everything is 0 and 1" — does this apply to code as well?**
Yes, both code and data are stored as sequences of 0s and 1s in memory. There is nothing in the bits themselves that distinguishes them — it is the CPU and the operating system that keep track of what is code and what is data.

**2. LIFO structure — and the opposite principle**
LIFO stands for Last In, First Out — the last item placed in is the first to be taken out. A stack of plates is a good everyday example: we always take from the top. The opposite principle is FIFO: First In, First Out — like a queue where the first to arrive is the first to leave.

**3. Statically typed vs. dynamically typed**
In statically typed languages like C++ and Java, the type of a variable must be declared explicitly and cannot change afterwards. In dynamically typed languages like Python, the type is determined at runtime, and a variable can refer to values of different types during the same program run.

**4. A line starting with `#`**
The line is ignored entirely — it is a comment and has no effect on the execution of the program.

**5. Why `int(input(...))`?**
`input()` always returns a text string, regardless of what the user types. `int()` converts the text string to an integer. Without the conversion, mathematical operations would not work as expected.

**6. `.py` file vs. REPL**
From a `.py` file the entire program runs from top to bottom, and only what is explicitly printed with `print()` is shown. In REPL one line is evaluated at a time, and expressions that produce a result are printed automatically without `print()`.

**7. What produces output in REPL?**

| Input | Output? | Explanation |
|---|---|---|
| `2 + 2` | Yes | Expression — the result is displayed automatically |
| `x = 2 + 2` | No | Assignment — produces no output |
| `print(2 + 2)` | Yes | Explicit print request |
| `def f(): return 5` | No | Function definition — produces no output |

---

## Practical — try in REPL

**8. `2 + 2` vs. `x = 2 + 2`**
Typing `2 + 2` in REPL evaluates the expression and immediately prints the result `4`. Typing `x = 2 + 2` assigns the value to `x` — nothing is printed because an assignment is a statement, not an expression that produces a value to display.

**9. `type()` on the basic types**
```
type(42)      → <class 'int'>
type(3.14)    → <class 'float'>
type("Hello") → <class 'str'>
type(True)    → <class 'bool'>
```

**10. Greeting with name and age**
```python
>>> name = "Ada"
>>> age = 25
>>> print("Hello,", name, "you are", age, "years old.")
Hello, Ada you are 25 years old.
```

**11. Integer division `//` and modulo `%`**
```
10 // 3  → 3    (integer part of 10 ÷ 3)
10 %  3  → 1    (remainder: 3 × 3 = 9, so 10 - 9 = 1)
17 // 5  → 3    (integer part of 17 ÷ 5)
17 %  5  → 2    (remainder: 5 × 3 = 15, so 17 - 15 = 2)
```
`//` gives the whole-number part of a division; `%` gives the remainder.

**12. `10 / 0` in REPL**
Python raises a `ZeroDivisionError: division by zero`. Division by zero is mathematically undefined and Python signals this with an exception that stops the program.

**13. The `add()` function with different types**
```python
>>> add(2, 3)       # two integers → 5   (int)
>>> add(2.0, 3.0)   # two floats   → 5.0 (float)
>>> add("Hi", "!")  # two strings  → "Hi!" (str concatenation)
```
Python's `+` operator is overloaded — its behaviour depends on the type of the operands. For integers and floats it performs arithmetic addition; for strings it performs concatenation.
