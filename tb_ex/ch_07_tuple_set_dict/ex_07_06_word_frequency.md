---
title: "Word Frequency"
id: "ex_07_06_word_frequency"
tags: ["dict", "dict views", "keys", "values", "items", "Counter", "collections"]
difficulty: "medium"
prerequisites: ["dict", "for", "str", "split", "sorted", "Counter"]
learning_outcomes:
  - "Build a frequency dict manually using get()"
  - "Use dict.keys(), dict.values() and dict.items()"
  - "Use Counter from collections as a Pythonic alternative"
  - "Use Counter.most_common() to get top results"
---

# Word Frequency

## Exercise

### Part 1 - Manual approach

Write a function `word_count(text: str) -> dict` that counts how often
each word appears in a text. Convert to lowercase and strip punctuation
before counting.

Use the result to:
- Display all words and their counts using `.items()`
- Find the total number of unique words using `.keys()`
- Find the most common word using `.values()` and `.items()`
- Check if a specific word appears using `in` (which checks `.keys()`)

### Part 2 - Counter

Rewrite `word_count` using `Counter` from the `collections` module.
Verify the result is identical.

Use `Counter.most_common(5)` to display the 5 most frequent words.

Use this text for testing:

```python
text = """to be or not to be that is the question
whether tis nobler in the mind to suffer
the slings and arrows of outrageous fortune
or to take arms against a sea of troubles"""
```

## Example run

```
--- Part 1: manual ---
Word counts (sorted):
  a          1
  against    1
  and        1
  ...
  the        3
  to         4

Unique words: 28
Most common:  to (4 times)
'fortune' in text: True

--- Part 2: Counter ---
Top 5 words:
  to:      4
  the:     3
  or:      2
  of:      2
  be:      2
```

## Topics

- `dict.keys()`, `dict.values()`, `dict.items()`
- Manual frequency counting with `get()`
- `Counter` and `most_common()`
- The contrast between manual and Pythonic approaches

---
## Instructor notes

**Learning objectives covered:** dict views, Counter, most_common

**Dict views are views, not copies:** Worth mentioning that keys(),
values() and items() return live views - they reflect changes to the
dict. Iterating them in a for loop is the standard pattern.

**Counter is a dict subclass:** Students can use all dict methods on
a Counter. `most_common()` is the main extra feature.

**Punctuation stripping:** `word.strip('.,!?;:\'"')` is sufficient for
this exercise. A more robust approach uses `str.translate()` but that
is beyond ch 7 scope.
