# Pythonic patterns – Chapter 7: Tuples, dictionaries and sets

## Swapping values

| Beginner | Pythonic |
|----------|----------|
| `temp = a`<br>`a = b`<br>`b = temp` | `a, b = b, a` |

Tuple unpacking makes value swapping elegant — no temporary variable needed.

## Tuple unpacking

| Beginner | Pythonic |
|----------|----------|
| `x = coordinate[0]`<br>`y = coordinate[1]` | `x, y = coordinate` |
| `name = person[0]`<br>`age = person[1]`<br>`_ = person[2]` | `name, age, _ = person` |

Direct unpacking is more readable and self-documenting than indexing.

## Dictionary lookup

| Beginner | Pythonic |
|----------|----------|
| `if "key" in d:`<br>`    val = d["key"]`<br>`else:`<br>`    val = 0` | `val = d.get("key", 0)` |

`get()` with a default value replaces the if/else check entirely.

## Counting occurrences

| Beginner | Pythonic |
|----------|----------|
| `if char in count:`<br>`    count[char] += 1`<br>`else:`<br>`    count[char] = 1` | `count[char] = count.get(char, 0) + 1` |
| `count[char] = count.get(char, 0) + 1` | `from collections import Counter`<br>`count = Counter(text)` |

Manual counting with `get()` is fine for simple cases. `Counter` is even more Pythonic when counting all elements in an iterable at once.

## Iterating over a dictionary

| Beginner | Pythonic |
|----------|----------|
| `for key in d:`<br>`    print(key, d[key])` | `for key, val in d.items():`<br>`    print(key, val)` |

`items()` gives both key and value directly — avoids a double lookup.

## Building a dictionary from two lists

| Beginner | Pythonic |
|----------|----------|
| `d = {}`<br>`for i in range(len(keys)):`<br>`    d[keys[i]] = values[i]` | `d = dict(zip(keys, values))` |

`zip()` combines the two lists into pairs; `dict()` builds the dictionary.

## Removing duplicates

| Beginner | Pythonic |
|----------|----------|
| `unique = []`<br>`for x in lista:`<br>`    if x not in unique:`<br>`        unique.append(x)` | `unique = list(set(lista))` |

Converting via `set` removes duplicates in one operation. Note that order is not preserved.

## Empty set

| Beginner | Pythonic |
|----------|----------|
| `s = {}  # wrong — this is a dict!` | `s = set()` |

`{}` always gives an empty dictionary. An empty set always requires `set()`.

## Subset check

| Beginner | Pythonic |
|----------|----------|
| `all(x in b for x in a)` | `a <= b` or `a.issubset(b)` |

Set operators are shorter and more mathematically precise.

## Finding the most common element

| Beginner | Pythonic |
|----------|----------|
| `count = {}`<br>`for x in lista:`<br>`    count[x] = count.get(x, 0) + 1`<br>`most_common = max(count, key=count.get)` | `from collections import Counter`<br>`most_common = Counter(lista).most_common(1)[0][0]` |

`Counter` with `most_common()` is the idiomatic solution for finding the most frequently occurring elements.
