# Chapter 2 – Answer Key: Review Questions

## 2.1–2.2 A program solves a task / Naming

**1. Constant vs. variable**
A variable can change value during execution and is named using snake_case, e.g. `current_year`. A constant is intended not to change and is named using UPPER_CASE, e.g. `CURRENT_YEAR`. Python does not enforce this — it is a convention only.

**2. Dynamically typed**
The type of a variable is determined at runtime, not declared in advance. A variable can refer to values of different types during the same program run. In C++ and Java, the type must be declared explicitly and cannot change to a different type afterwards.

**3. snake_case**
snake_case uses lowercase letters with underscores between words, e.g. `student_count`. Variables, functions, parameters, and filenames should follow this convention in Python.

---

## 2.3 Operator precedence and associativity

**4. Precedence vs. associativity**
Precedence defines the ranking of operators — some are evaluated before others. Associativity defines the direction in which an expression is read when two operators of the same precedence appear in sequence.

**5. Unary vs. binary operator**
A binary operator takes two operands: `1 + 2` — `+` has operands `1` and `2`. A unary operator takes one operand: `-5` — `-` is unary with operand `5`.

---

## 2.4 The int and float numerical data types

**6. int vs. float**
`int` is a whole number (e.g. `2`, `17`, `-5`), `float` is a decimal number (e.g. `2.0`, `3.14`). Use `int` for whole quantities such as age or count, `float` for measurements and calculations that require decimals.

**7. Why `0.1 + 0.2 == 0.3` gives `False`**
Decimal numbers are stored internally as binary fractions, which cannot always be represented exactly. `0.1 + 0.2` produces `0.30000000000000004` internally, which is not precisely equal to `0.3`. To compare floats we should check whether the difference is smaller than a small tolerance, e.g. `abs(a - b) < 1e-9`, or use `math.isclose()`.

**8. The difference between `/` and `//`**
`/` is regular division and always returns `float`. `//` is floor division and returns only the integer part of the result. Given `7` and `2`: `7 / 2` → `3.5`, `7 // 2` → `3`.

**9. Immutable int**
The value cannot be changed at the same memory address. When we write `a = 20` after `a = 10`, Python creates a new object at a new address — the old value is lost and eventually cleaned up by the garbage collector.

**10. `type()`, `id()` and `dir()`**
`type()` returns the type of an object, e.g. `<class 'int'>`. `id()` returns the unique memory address of an object — useful for checking whether two variables point to the same object. `dir()` lists all attributes and methods available on an object — useful for exploring what we can do with a value.

---

## 2.5 The str data type

**11. Why `str` is immutable**
Strings cannot be changed after they are created. Methods such as `.upper()` return a new string — they do not modify the original.

**12. Escape sequences**
An escape sequence is a combination of `\` and a character that together represent a special character. `\n` is a newline, `\t` is a tab, `\\` is a literal backslash.

**13. Raw string**
A string prefixed with `r` in which escape sequences are not interpreted. Useful for file paths: `r"C:\Users\Ola"` instead of `"C:\\Users\\Ola"`.

**14. `.find()` vs. `.index()`**
Both return the index of the first occurrence of a substring. `.find()` returns `-1` if the substring is not found, while `.index()` raises a `ValueError`.

---

## 2.6 The bool data type

**15. Truthiness**
Truthiness means that Python values can be interpreted as `True` or `False`. For `int`: only `0` gives `False`. For `float`: only `0.0` gives `False`. For `str`: only the empty string `""` gives `False`.

**16. `None`**
`None` is Python's way of expressing "no value" or "nothing here". It is not the same as `0`, `False`, or `""` — those are actual values. `None` is its own type (`NoneType`) and is often used as a default or placeholder value.

---

## 2.7 Conversions between int, float, str, and bool

**17. Why `input()` always returns a string**
`input()` is designed to read text from the keyboard. We must convert explicitly with `int()` or `float()` if we need a number.

**18. Invalid conversion**
`int("abc")` raises a `ValueError` because `"abc"` cannot be interpreted as a whole number. `int("25")` works fine and gives `25`.

---

## 2.8 The input() function

**19. Coding pattern**
An established solution to a problem that recurs again and again. Not a rule, but a convention experienced programmers have settled on because it is clear and easy to recognise.

**20. Pythonic code**
Code that solves the problem the way Python is designed for — concise and readable. Example: `age = int(input("Age: "))` is more Pythonic than splitting it into two lines without reason.

**21. Why chain `.strip()` and `.lower()`**
`.strip()` removes unintentional whitespace; `.lower()` makes comparisons case-insensitive. Chained on input, `"YES"`, `"Yes"` and `" yes "` all produce `"yes"`.

---

## 2.9 The print() function

**22. Default behaviour of `print()`**
Space between arguments (`sep=" "`) and a newline after the last argument (`end="\n"`). Both can be overridden by passing explicit `sep` or `end` keyword arguments.

---

## 2.10 Use and misuse of comments

**23. The main rule for comments**
Use comments to explain *why* the code does something, not *what* it does. The code itself should show what is happening — good names make comments redundant.

**24. Docstring**
A triple-quoted string placed immediately after a function or class definition. Accessible via `help()` and used by development tools such as VSCode to display documentation. Unlike regular comments, docstrings are stored as part of the object at runtime.

---

## 2.11 A first look at the math module

**25. `**` vs. `math.pow()`**
`**` returns `int` when both operands are `int` (e.g. `2 ** 3` gives `8`). `math.pow()` always returns `float` (e.g. `math.pow(2, 3)` gives `8.0`).

**26. `math.ceil()` and `math.floor()`**
`math.ceil()` rounds up to the nearest integer: `math.ceil(4.1)` gives `5`. `math.floor()` rounds down: `math.floor(4.9)` gives `4`.

**27. Why `import math`**
`math` is a module that is not loaded automatically. `import math` makes all functions in the module available.

---

## 2.12 A first look at the random module

**28. `random.randint(1, 6)` and endpoints**
Returns a random integer between 1 and 6. Both endpoints are inclusive — `randint(1, 6)` can return both `1` and `6`.

**29. `random.randint()` vs. `random.random()`**
`random.randint(a, b)` returns a random integer between `a` and `b` (both inclusive). `random.random()` returns a random float between `0.0` and `1.0` (0.0 inclusive, 1.0 exclusive).

**30. Seed**
A starting value for the random number generator. With the same seed, the same sequence of "random" numbers is always produced. Useful for testing and reproducible results — we can recreate an exact sequence even when randomness is involved.

**31. Pseudorandom numbers**
A computer is deterministic — it always does the same thing given the same input. True randomness does not exist in a CPU. `random` uses a mathematical formula that produces numbers that look random but are completely predictable if we know the seed. Hence the prefix *pseudo* — "apparently".

---

## 2.13 Formatting text with f-strings

**32. What is an f-string**
A string prefixed with `f` that can contain placeholders `{}` with variables or expressions that are evaluated when the string is created.

**33. What is a placeholder**
An expression enclosed in `{}` in an f-string. It can contain variables, arithmetic expressions, method calls, and format specifiers.

**34. `:.2f` vs. `:.2e`**
`:.2f` gives two decimal places in standard notation: `12.57`. `:.2e` gives two decimal places in scientific notation: `1.26e+01`.

**35. Default alignment for text and numbers**
Text (`str`) is left-aligned by default. Numbers (`int` and `float`) are right-aligned by default. Override with `<` (left), `>` (right), or `^` (centre).

---

## Practical

**Operator precedence — evaluate by hand**

```
2 + 3 * 4     → multiplication first: 2 + 12 = 14
10 - 2 ** 3   → exponentiation first: 10 - 8 = 2
2 ** 3 ** 2   → right-to-left: 2 ** 9 = 512
not True or False → not binds tightest: False or False = False
```

**Bool conversions — REPL**

```
bool(0)       → False
bool("")      → False
bool([])      → False   (empty list — covered later)
bool(None)    → False
bool(-1)      → True    (any non-zero int)
bool("False") → True    (non-empty string)
```

**Slicing `text = "Hello, world!"`**

```
text[0]                  → 'H'
text[-1]                 → '!'
text[0:5]                → 'Hello'
text[7:]                 → 'world!'
text[::-1]               → '!dlrow ,olleH'
text.upper()             → 'HELLO, WORLD!'
text.replace("world", "Python") → 'Hello, Python!'
```

**Sum, difference, product, quotient, remainder**

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print(f"Sum:       {a + b}")
print(f"Difference:{a - b}")
print(f"Product:   {a * b}")
print(f"Quotient:  {a / b}")
print(f"Remainder: {a % b}")
```

**First and last name with split()**

```python
full_name = input("Enter first and last name: ")
first, last = full_name.split()
print(f"Hello, {first} {last}! Initials: {first[0]}.{last[0]}.")
```

**City comparison — case-insensitive**

```python
city = input("Enter a city: ").strip().lower()
if city == "oslo":
    print("The city is Oslo.")
else:
    print("The city is not Oslo.")
```

**Circle area with math.pi**

```python
import math
radius = float(input("Radius: "))
area = math.pi * radius ** 2
print(f"Area: {area:.2f}")
```

**Distance between two points**

```python
import math
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance: {distance:.2f}")
```

**Seed and reproducibility**

```python
import random
random.seed(0)
for _ in range(5):
    print(random.randint(1, 10))
```

Running the program twice produces exactly the same five numbers both times. Without `seed(0)`, the numbers would differ on every run.

**Sentence analysis**

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")
print(f"Uppercase: {sentence.upper()}")
if "python" in sentence.lower():
    print("The sentence contains the word 'python'.")
else:
    print("The sentence does not contain the word 'python'.")
```

**Handle non-numeric input**

```python
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(f"Sum: {a + b}")
except ValueError:
    print("Error: please enter valid numbers.")
```

*Note: `try/except` is covered properly in a later chapter — this is a preview.*

**Dice simulation — sum of 7**

```python
import random
count = 0
for _ in range(1000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        count += 1
print(f"Sum of 7 occurred {count / 1000:.1%} of the time.")
```

**Read until non-empty input**

```python
name = ""
while not name.strip():
    name = input("Enter your name: ")
print(f"Hello, {name.strip()}!")
```

**Table: name, age, monthly salary**

```python
print(f"{'Name':<15} {'Age':>6} {'Annual salary':>15}")
for _ in range(3):
    name         = input("Name: ")
    age          = int(input("Age: "))
    monthly_pay  = float(input("Monthly salary: "))
    annual_pay   = monthly_pay * 12
    print(f"{name:<15} {age:>6} {annual_pay:>15,.2f}")
```

**Extended table with tax deduction**

```python
print(f"{'Name':<15} {'Age':>6} {'Annual salary':>15} {'Tax (33%)':>12}")
for _ in range(3):
    name         = input("Name: ")
    age          = int(input("Age: "))
    monthly_pay  = float(input("Monthly salary: "))
    annual_pay   = monthly_pay * 12
    tax          = annual_pay * 0.33
    print(f"{name:<15} {age:>6} {annual_pay:>15,.2f} {tax / annual_pay:>11.1%}")
```
