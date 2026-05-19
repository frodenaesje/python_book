# Chapter 7 – Answer Key: Review Questions

## Understanding

**1. tuple vs. list**
A tuple is immutable — it cannot be changed after it is created. A list is mutable. Tuples are used when data should not change, are faster than lists, and can be used as keys in a dictionary.

**2. Single-value tuple**
`(42)` is just a number in parentheses — Python interprets it as a regular `int`. The comma is what tells Python this is a tuple: `(42,)`. Without the comma there is no tuple.

**3. Tuple unpacking**
Unpacking extracts elements from an iterable and assigns them to separate variables in one operation. The technique works on all iterables — tuples, lists, strings, and anything else Python can iterate over.

**4. The starred expression `*`**
The variable that receives `*` collects all elements not explicitly assigned elsewhere. The type is always `list`, even when unpacking from a tuple.

**5. `[]` vs. `get()`**
`[]` raises a `KeyError` if the key is not found. `get()` returns `None` by default, or an optional fallback value we specify: `get("key", 0)`. Use `get()` when the key may be absent.

**6. Dynamic dictionary views**
`keys()`, `values()` and `items()` do not return copies — they return live views that automatically reflect changes in the dictionary. Adding or removing a key is immediately visible in the view without calling the method again.

**7. Hashability**
A hashable value has a constant hash value throughout its lifetime and can be compared with other values. Python uses `hash(key)` to place and find values quickly in the dictionary's internal hash table. The key must be hashable for lookups to work consistently.

**8. `list` vs. `tuple` as a key**
`list` is mutable — its contents can change after creation, which would make the hash value unstable and lookups unreliable. `tuple` is immutable — its hash value is constant, so it can be used as a key.

**9. `remove()` vs. `discard()`**
`remove()` raises a `KeyError` if the element is not found. `discard()` does nothing if the element is not found. Use `discard()` when you are not certain the element is in the set.

**10. First four vs. last four set operations**
The first four (`|`, `&`, `-`, `^`) create a new set and leave the originals unchanged. The last four (`|=`, `&=`, `-=`, `^=`) modify the first set in place.

**11. `{}` is always a dictionary**
Python determines the type from the contents: `{"a": 1}` is a dict because it has a colon between key and value; `{1, 2}` is a set because it has only values. But `{}` is empty — no colon, no values — and Python defaults to dictionary. An empty set must be created with `set()`.

**12. `TypedDict`**
`TypedDict` lets us specify exactly which keys a dictionary should have and what type each value has. Regular type hints like `dict[str, int]` only say something about the types in general, not which specific keys should be present. `TypedDict` gives the IDE enough information to warn about wrong keys and provide precise autocompletion.

**13. `Counter`**
`Counter` is a specialised dictionary from the `collections` module where the keys are elements from an iterable and the values are counts of occurrences. It resembles `dict` most closely, but gives us `most_common()` as a bonus and sorts by frequency when printed.

**14. Requirements for elements in `Counter`**
The elements being counted must be hashable — the same requirement as for dictionary keys. Strings, numbers and tuples are hashable. Lists and dictionaries are not hashable and cannot be counted directly. The iterable argument to `Counter` itself may be a list.

**15. `most_common(2)` and `most_common()`**
`most_common(n)` returns the `n` most frequently occurring elements as a list of `(element, count)` tuples, sorted from most to least common. `most_common()` without an argument returns all elements in the same order.

---

## Practical

**16. Unpacking and swapping**
```python
t = (10, 20, 30)
a, b, c = t
a, b = b, a
print(a, b, c)  # 20 10 30
```

**17. Extended unpacking**
```python
t = (1, 2, 3, 4, 5, 6)
first, *middle, last = t
print(first)   # 1
print(middle)  # [2, 3, 4, 5]
print(last)    # 6
```

**18. Dictionary — countries and capitals**
```python
capitals = {
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Denmark": "Copenhagen"
}
capitals["Finland"] = "Helsinki"         # add
capitals["Norway"] = "Oslo (updated)"   # change
capitals.pop("Denmark")                  # remove
print(capitals)
```

**19. Iterate with `items()`**
```python
capitals = {"Norway": "Oslo", "Sweden": "Stockholm", "Finland": "Helsinki"}
for country, capital in capitals.items():
    print(f"{country:<15} {capital}")
```

**20. Count characters in a string**
```python
text = "mississippi"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
    print(f"'{char}': {count}")
```
`get(char, 0)` avoids having to check whether the key exists before adding 1. This is the standard pattern for counting with a dictionary.

**21. Set operations**
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a & b)  # {3, 4}
print(a - b)  # {1, 2}
```

**22. Remove duplicates with set**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = set(numbers)
print(len(unique))  # 7
```

**23. Subset check**
```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a <= b)          # True — a is a subset of b
print(a.issubset(b))   # same, using the method
```

**24. `Counter` — letters in a name**
```python
from collections import Counter

name = "Mississippi"
c = Counter(name.lower())
print(c)
print(c.most_common(1))  # most common letter
```

**25. `Counter` — most common words**
```python
from collections import Counter

text = "once upon a time there was a little man who had a cat"
words = text.split()
c = Counter(words)
print(c)
# Counter({'a': 3, 'once': 1, 'upon': 1, ...})
print(c.most_common(3))
# [('a', 3), ('once', 1), ('upon', 1)]
```
