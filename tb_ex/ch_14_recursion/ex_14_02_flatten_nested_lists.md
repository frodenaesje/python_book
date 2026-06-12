---
title: "Flatten Nested Lists"
id: "ex_14_02_flatten_nested_lists"
tags: ["recursion", "list", "isinstance", "extend", "linear recursion"]
difficulty: "easy"
prerequisites: ["recursion", "base case", "list", "isinstance"]
learning_outcomes:
  - "Write a recursive function that processes a list element by element"
  - "Use isinstance() to distinguish between list and non-list elements"
  - "Understand how extend() merges a recursive result into the current level"
---

# Flatten Nested Lists

## Exercise

A nested list is a list that may contain other lists as elements, to
any depth. Write a recursive function `flatten(nested_list)` that
returns a single flat list containing all the non-list elements.

Rules:
- If an element is a list, call `flatten()` recursively on it and
  extend the result into the flat list
- If an element is not a list, append it directly
- Return the flat list

## Example run

```
flatten([1, [2, 3], 4])
-> [1, 2, 3, 4]

flatten([1, [2, [3, 4]], 5])
-> [1, 2, 3, 4, 5]

flatten([1, 2, 3])
-> [1, 2, 3]

flatten([1, [2, [3, [4, [5]]]]])
-> [1, 2, 3, 4, 5]
```

## Extension

Rewrite `flatten()` as a generator using `yield` and `yield from`.
Compare the two implementations.

## Topics

- Recursion on a variable-depth structure
- `isinstance(item, list)` to branch on type
- `list.extend()` to merge recursive results
- Generator version with `yield from` (extension)

---
## Instructor notes

**Learning objectives covered:** recursion on nested structures, isinstance,
extend vs append

**Why extend not append:** `flat_list.append(flatten(item))` would add the
whole sublist as one element - the opposite of what we want. `extend` adds
each element individually.

**Generator version:**
```python
def flatten_gen(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_gen(item)
        else:
            yield item
```
`yield from` delegates to another generator - a clean pattern worth
showing alongside the list version.
