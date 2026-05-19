# Chapter 4 – Answer Key: Review Questions

## Conditions and operators

**1. `=` vs. `==`**
`=` is assignment — it sets a variable to a value. `==` is comparison — it returns `True` or `False`. Writing `if x = 5` is a syntax error in Python, unlike C++ and Java where it is legal but often a bug.

**2. True/False expressions**
```
a) 10 > 5          → True
b) 10 == 10.0      → True   (Python compares values, not types)
c) "hei" == "Hei"  → False  (case-sensitive)
d) 5 != 5          → False
```

**3. Operator precedence**
The order is: arithmetic operators first, then relational (`>`, `<`, `==` etc.), then `not`, then `and`, and finally `or`. Example: `a > 5 and b < 5 or a == 10` is evaluated as `(a > 5 and b < 5) or (a == 10)` — `and` binds more tightly than `or`.

**4. Chained comparison**
`8 <= start_time < 18` is a chained comparison that checks that `start_time` is between 8 and 18. The advantage over `start_time >= 8 and start_time < 18` is that it is shorter, more readable, and evaluates `start_time` only once.

---

## Code blocks and if-else structures

**5. Code block in Python**
A code block is a group of lines that belong together, marked by indentation — typically 4 spaces. In C++, Java and C# blocks are marked with `{}` and indentation is for readability only. In Python the indentation *is* the structure — wrong indentation causes either an `IndentationError` or a silent logical error.

**6. One-way, two-way, and if-elif-else**
A one-way `if` runs a block only if the condition is true; otherwise nothing happens. A two-way `if-else` always gives one of two outcomes. `if-elif-else` handles multiple mutually exclusive alternatives. `elif` is preferable to nested `if-else` when comparing one variable against several values — the code stays flat and is easier to read.

**7. Wrong indentation**
With `temperature = 15`, `"put on your jacket."` is always printed, regardless of temperature — the line is not part of the `if` block. The intention was probably that both `print()` calls should belong to the `if` block.

---

## Ternary operator, pass and walrus

**8. Guard clauses**
Guard clauses are early `return` (or `exit`) statements at the top of a function that handle invalid states first. The advantage is that we avoid deep nesting — the main logic can be written flat, without extra indentation levels.

**9. `pass`**
`pass` is a null-operation statement — a syntactic placeholder that does nothing. Python requires at least one statement in every code block, and `pass` fills that role during development when we want to sketch the structure without implementing everything. A better alternative in classes and functions is a docstring, which counts as a statement and simultaneously documents the intent.

**10. The walrus operator `:=`**
The walrus operator assigns a value to a variable and evaluates that value in the same expression. The difference from regular `=` is that `:=` is an expression — it has a value — and can be used inside `if` conditions and `while` loops. Useful for avoiding computing something twice:

```python
# Without walrus — calls len() twice
if len(data) > 10:
    print(f"Large list with {len(data)} elements")

# With walrus — computed once
if (n := len(data)) > 10:
    print(f"Large list with {n} elements")
```

---

## match-case

**11. `case _:`**
`case _:` is the wildcard case and matches anything not caught by earlier `case` branches. It is the equivalent of `else` in an `if-elif` chain.

**12. match-case vs. if-elif**
`match-case` is preferable when comparing one variable against several fixed values — the code becomes cleaner and the intent clearer. `if-elif` is still natural when conditions are compound expressions, ranges, or combine multiple variables.

---

## Truthiness and None

**13. Falsy values**
A falsy value is one that Python interprets as `False` in a condition. Falsy values: `0` (int), `0.0` (float), `""` (empty string), `None`. Everything else is truthy.

**14. `None`**
`None` is Python's way of representing "no value" or "not set". It is not the same as `0`, `False` or `""` — it is its own type (`NoneType`) and means explicitly absent value.

**15. `if name:` vs. `if name is not None:`**
`if name:` is a truthiness check and gives `False` for both `None`, empty string, and other falsy values. `if name is not None:` explicitly checks only whether the value is `None` — an empty string would give `True`. Use `is not None` when an empty string is a valid answer that should be treated differently from "not set".

---

## Practical

**16. REPL — boolean expressions**
```
a) 5 > 3 and 10 < 20   → True   (both true)
b) 5 > 3 or 10 > 20    → True   (first operand is true)
c) not (5 == 5)         → False  (negation of True)
d) 5 > 3 and not 10 > 20 → True  (True and not False → True and True)
```

**17. REPL — precedence**
```python
a = 10
b = 3
print(a > b and b > 0)          # True  (both True)
print(a > b or b > 20)          # True  (first operand is True)
print(not a == b)               # True  (not False)
print(a > 5 and b < 5 or a == 10)  # True
```
Last line: `and` binds before `or` → `(True and True) or True` → `True`.

**18. Positive, negative or zero**
```python
number = int(input("Enter an integer: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**19. Ticket prices**
```python
age = int(input("Enter your age: "))
if age < 16:
    print("Ticket price: 50 NOK")
elif 16 <= age < 67:
    print("Ticket price: 120 NOK")
else:
    print("Ticket price: 80 NOK")
```

**20. Off-by-one error — `age > 18`**
With `age = 18` the program prints `"You are too young."` The condition `age > 18` excludes 18-year-olds. The fix is `age >= 18`.

**21. Ternary operator**
```python
text = "item" if count == 1 else "items"
print(f"You have {count} {text}.")
```

**22. Guard clauses**
```python
score = 85

if score < 0:
    print("Score cannot be negative.")
elif score > 100:
    print("Score cannot exceed 100.")
elif score >= 90:
    grade = "A"
    print(f"Grade: {grade}")
elif score >= 75:
    grade = "B"
    print(f"Grade: {grade}")
else:
    grade = "C"
    print(f"Grade: {grade}")
```

Guard clauses remove the deep nesting. The invalid cases are handled first and flatly — the rest of the code can be written without extra indentation levels.

**23. Walrus operator — read until empty**
```python
while (line := input("Type something: ").strip()):
    print(f"You typed: {line}")
# Stops when the user presses Enter without typing anything
```

**24. Month names with match-case**
```python
month = int(input("Enter a month number (1-12): "))
match month:
    case 1:  print("January")
    case 2:  print("February")
    case 3:  print("March")
    case 4:  print("April")
    case 5:  print("May")
    case 6:  print("June")
    case 7:  print("July")
    case 8:  print("August")
    case 9:  print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")
    case _:  print("Invalid month number")
```

**25. Truthiness — REPL**
```
a) bool(0)    → False   (zero int)
b) bool("")   → False   (empty string)
c) bool(" ")  → True    (non-empty string)
d) bool(None) → False
e) bool([])   → False   (empty list — covered later)
```

**26. Pythonic rewrites**
```python
# Original:                        # Pythonic:
if len(name) > 0:                  if name:
    print("Name provided")             print("Name provided")

if is_active == True:              if is_active:
    print("Active")                    print("Active")

if count != 0:                     if count:
    print("Elements exist")            print("Elements exist")
```

**27. Leap year**
```python
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

The order is crucial — the 400 rule must be checked before the 100 rule, otherwise year 2000 would be incorrectly rejected. Test cases: 2000 (leap), 1900 (not), 2024 (leap), 2001 (not).
