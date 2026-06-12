---
title: "Tuple, Set and Dict Comprehensions"
id: "ex_07_08_comprehensions"
tags: ["tuple comprehension", "set comprehension", "dict comprehension", "list comprehension"]
difficulty: "easy"
prerequisites: ["for", "list comprehension", "tuple", "set", "dict"]
learning_outcomes:
  - "Convert for loops to set comprehensions"
  - "Convert for loops to dict comprehensions"
  - "Use tuple() with a generator expression"
  - "Add filter conditions to comprehensions"
---

# Tuple, Set and Dict Comprehensions

## Exercise

Convert each of the following for loops to a comprehension.

### Tuple comprehensions

**Example 1** - squares of numbers 0-5:
```python
result = ()
for i in range(6):
    result += (i**2,)
```

**Example 2** - pairs (number, square) for even numbers 0-10:
```python
result = ()
for i in range(0, 11, 2):
    result += ((i, i**2),)
```

### Set comprehensions

**Example 3** - unique letters in "hello":
```python
word = "hello"
result = set()
for char in word:
    result.add(char)
```

**Example 4** - lengths of words starting with 'a' or 'b':
```python
words = ["apple", "apricot", "banana", "cat", "blueberry", "dog"]
result = set()
for word in words:
    if word[0] in ('a', 'b'):
        result.add(len(word))
```

### Dict comprehensions

**Example 5** - numbers 0-4 mapped to their squares:
```python
result = {}
for i in range(5):
    result[i] = i**2
```

**Example 6** - words mapped to their lengths, only for words longer than 3:
```python
words = ["apple", "cat", "banana", "dog", "elephant", "ox"]
result = {}
for word in words:
    if len(word) > 3:
        result[word] = len(word)
```

## Topics

- `tuple(expr for x in iterable)` syntax
- `{expr for x in iterable}` set comprehension
- `{key: value for x in iterable}` dict comprehension
- Filter conditions with `if`

---
## Instructor notes

**Learning objectives covered:** all three comprehension forms, filter conditions

**Tuple note:** There is no `{...}` syntax for tuples - use `tuple(generator)`.
This is worth explaining: `(x**2 for x in range(6))` is a generator expression,
not a tuple. Wrapping with `tuple()` materializes it.

**Verify:** Students should print both the loop version and the comprehension
version and confirm identical output.
