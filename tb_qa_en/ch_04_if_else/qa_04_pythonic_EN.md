# Pythonic code – Chapter 4

## Comparing with True/False

Avoid comparing directly against `True` or `False` — use the value directly.

```python
# Beginner
if is_active == True:
    print("Active")

# Pythonic
if is_active:
    print("Active")
```

## Truthiness — avoid unnecessary length checks

```python
# Beginner
if len(name) > 0:
    print("Name provided")

if count != 0:
    print("Elements exist")

# Pythonic
if name:
    print("Name provided")

if count:
    print("Elements exist")
```

## Ternary operator

For simple two-way choices the ternary operator is more compact than if-else.

```python
# Beginner
if count == 1:
    text = "item"
else:
    text = "items"

# Pythonic
text = "item" if count == 1 else "items"
```

Rule of thumb: if you cannot read the expression aloud in one sentence and understand it immediately, use regular if-else.

## Chained comparison

```python
# Beginner
if start_time >= 8 and start_time < 18:
    print("Daytime")

# Pythonic
if 8 <= start_time < 18:
    print("Daytime")
```

## Guard clauses instead of deep nesting

```python
# Beginner — deep nesting
def process(score):
    if score >= 0:
        if score <= 100:
            if score >= 90:
                grade = "A"
            else:
                grade = "B"
            print(f"Grade: {grade}")
        else:
            print("Too high")
    else:
        print("Negative")

# Pythonic — guard clauses
def process(score):
    if score < 0:
        print("Negative")
        return
    if score > 100:
        print("Too high")
        return
    grade = "A" if score >= 90 else "B"
    print(f"Grade: {grade}")
```

## pass — use a docstring instead where possible

```python
# Beginner
class FigureError(Exception):
    pass

# Pythonic — self-documenting
class FigureError(Exception):
    """Base exception for all figure-related errors."""
```

`pass` is necessary in if-blocks and loops where a docstring makes no sense. In classes and functions a docstring is preferable because the code becomes self-documenting.

## Walrus — avoid computing twice

```python
# Beginner — calls len() twice
if len(data) > 10:
    print(f"Large list with {len(data)} elements")

# Pythonic — computed once
if (n := len(data)) > 10:
    print(f"Large list with {n} elements")
```

Walrus is also useful in while loops where we want to read and test in one expression:

```python
# Beginner — duplicated input call
text = input("Type something: ").strip()
while text:
    print(f"You typed: {text}")
    text = input("Type something: ").strip()

# Pythonic
while (text := input("Type something: ").strip()):
    print(f"You typed: {text}")
```

Use walrus with care — where it clearly eliminates duplication, not just because it is possible.

## match-case instead of long if-elif chains

When comparing one variable against several fixed values, `match-case` is cleaner than `if-elif`.

```python
# Beginner
if day == 1:
    name = "Monday"
elif day == 2:
    name = "Tuesday"
elif day == 3:
    name = "Wednesday"
else:
    name = "Unknown"

# Pythonic
match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case _:
        name = "Unknown"
```

Note: `match-case` was introduced in Python 3.10. We will return to more advanced use of `match-case` in a later chapter.
