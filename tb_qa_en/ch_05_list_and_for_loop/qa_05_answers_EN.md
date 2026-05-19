# Chapter 5 – Answer Key: Review Questions

## Understanding

**1. Container vs. sequence**
Container is a conceptual term for data structures that hold multiple elements. Sequence is more specific: an ordered collection with an index per element. The sequence property gives us indexing, slicing, iteration with a for loop, `len()`, and operators like `in`, `+` and `*`.

**2. `list2 = list1`**
This copies only the reference — `list1` and `list2` point to the same list object in memory. Changes via `list2` are visible in `list1` and vice versa. `id()` returns the memory address of an object; `id(list1) == id(list2)` confirms they point to the same object.

**3. Shallow copy**
Creates a new list object, but fills it with the same references as the original. Works as expected when the list contains immutable elements (numbers, strings) — changes to the copy do not affect the original. Falls short when the list contains mutable objects (e.g. lists within a list) — the references to the inner objects are shared.

**4. `list.copy()` vs. `copy.deepcopy()`**
`list.copy()` makes a shallow copy — a new list object, but with shared references to the elements. `copy.deepcopy()` makes a complete copy of everything, recursively — original and copy are fully independent at all levels.

**5. `sort()` vs. `sorted()`**
`sort()` is a method on the list class that sorts the list in place and returns `None`. `sorted()` is a built-in function that returns a new, sorted list — the original is unchanged.

**6. The iteration variable as a copy**
`number` is a copy of each element, not a reference to a position in the list. Assigning to `number` does not affect the list. Technique 2 (`range(len(...))`) and technique 3 (`enumerate()`) both provide an index, which can be used to modify the list directly via indexing.

**7. `list(text)` vs. `[text]`**
`list(text)` iterates over the string character by character and creates a list of single characters: `["p", "y", "t", "h", "o", "n"]`. `[text]` creates a list with the string as a single element: `["python"]`.

**8. Range object**
A range object generates numbers on demand (lazy evaluation) instead of storing them all in memory. `range(0, 1_000_000)` uses almost no memory, while an equivalent list would store one million int objects.

**9. `s[::-1]`**
Reverses the sequence. Default values when the step is negative: start → last element, stop → before the first element. The result is a new sequence with the elements in reverse order.

**10. Slicing on the left side**
`list1[1:1] = [99, 100]` inserts two elements before index 1. `[1:1]` refers to an empty area between element 0 and element 1 — no elements are replaced, but it is a valid position for insertion.

**11. List comprehension**
A compact shorthand for for loops. `[x * x for x in range(10) if x % 2 != 0]` written as a regular for loop:
```python
result = []
for x in range(10):
    if x % 2 != 0:
        result.append(x * x)
```

**12. `join()`**
Requires all elements to be of type `str`. If the list contains numbers or other types we must convert them first, e.g. with a list comprehension: `", ".join([str(n) for n in numbers])`.

**13. `for` vs. `while`**
`for` is used when we iterate over a sequence or know in advance how many times to repeat. `while` is used when we do not know the number of iterations in advance, but want to continue as long as a condition is true. Rule of thumb: use `for` when iterating over something, `while` when waiting for something.

**14. Infinite loop**
A loop where the condition never becomes false, typically because we have forgotten to update the variable the condition depends on. Interrupted in the terminal with Ctrl+C.

**15. Duplicated input vs. `while True`**
In example 2a, `input()` must be called in two places — once before the loop to have a value to test the condition against, and once inside the loop to read the next value. `while True` with `break` solves this by reading input in only one place, and the exit condition is checked naturally where it belongs — after the value has been read.

**16. `all([])` and `any([])`**
`all([])` returns `True` and `any([])` returns `False`. This is mathematical convention: "all elements in an empty collection satisfy the condition" is true by definition (vacuous truth), while "at least one element satisfies the condition" is false when there are no elements.

**17. `map()` and `filter()` — why `list()`**
`map()` and `filter()` return lazy iterators — they do not compute values until requested. We must call `list()` to materialise all the values into a finished list. This is memory-efficient for large data sets since we only compute what we actually use.

**18. `zip()` with different lengths**
`zip()` stops when the shortest iterable is exhausted. Elements from the longer iterables that have no partner are silently ignored.

**19. `sorted(list)` vs. `list.sort()`**
`sorted()` returns a new sorted list and leaves the original unchanged. `list.sort()` sorts in place and returns `None` — a common mistake is writing `list = list.sort()`, which sets `list` to `None`.

**20. The `key` parameter**
`key` takes a function that is called on each element to compute a sort key. The element with the lowest key value comes first. The elements themselves are unchanged — only the order changes.

---

## Practical

**21. Empty list with names**
```python
names = []
names.append("Anna")
names.append("Bjorn")
names.append("Clara")
names.append("Dag")
names.append("Eva")
print(names[-1])   # Eva
print(names[-2])   # Dag
```

**22. Read five integers**
```python
numbers = []
for _ in range(5):
    numbers.append(int(input("Number: ")))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
```

**23. `sort()` vs. `sorted()`**
```python
numbers = [5, 3, 8, 1, 9, 2]
numbers.sort()
print(numbers)          # [1, 2, 3, 5, 8, 9] — original is changed

numbers = [5, 3, 8, 1, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)   # [1, 2, 3, 5, 8, 9]
print(numbers)          # [5, 3, 8, 1, 9, 2] — original unchanged
```

**24. Double every element**
```python
numbers = [1, 2, 3, 4, 5]
for index in range(len(numbers)):
    numbers[index] *= 2
print(numbers)  # [2, 4, 6, 8, 10]
```

**25. Months numbered from 1**
```python
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
for number, month in enumerate(months, start=1):
    print(f"{number}: {month}")
```

**26. Copy with `copy()`**
```python
original = [10, 20, 30]
copy = original.copy()
copy[0] = 99
print(original)  # [10, 20, 30] — unchanged
print(copy)      # [99, 20, 30]
```

**27. Slicing**
```python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[::2])   # [0, 2, 4, 6, 8] — every other element
print(lista[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] — reversed
```

**28. List comprehension — even numbers**
```python
even_numbers = [x for x in range(21) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**29. 3×3 matrix**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row_index, row in enumerate(matrix):
    print(f"Row {row_index}: {row}")
```

**30. `join()`**
```python
words = ["Python", "is", "fun"]
print(" ".join(words))  # Python is fun
```

**31. Guess a number**
```python
secret = 7
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You used {attempts} attempt(s).")
        break
    print("Wrong, try again.")
```

**32. Infinite loop — REPL**
```python
x = 1
while x > 0:
    x += 1
```
`x` increases every round and will never become ≤ 0, so the loop runs until we interrupt with Ctrl+C. Fix: change the condition to `while x < 10` or add `if x > 1000: break` inside the loop.

**33. `all()` — word length**
```python
words = ["hi", "hey", "hello"]
print(all(len(w) > 3 for w in words))   # False  ("hi" and "hey" have ≤ 3)

words = ["hey", "hello", "world"]
print(all(len(w) > 3 for w in words))   # True
```

**34. `map()` — uppercase**
```python
word_list = ["hello", "world", "python"]
upper = list(map(str.upper, word_list))
print(upper)  # ['HELLO', 'WORLD', 'PYTHON']

# Same with list comprehension
upper = [w.upper() for w in word_list]
```

**35. `filter()` — remove negatives**
```python
numbers = [3, -1, 4, -1, 5, -9, 2]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [3, 4, 5, 2]

# Same with list comprehension
positive = [x for x in numbers if x > 0]
```

**36. `zip()` — create dictionary**
```python
keys   = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

**37. `sorted()` with `key`**
```python
word_list = ["banana", "apple", "kiwi", "orange"]
print(sorted(word_list, key=len))                   # shortest first
print(sorted(word_list, key=len, reverse=True))     # longest first
```

**38. Three dice — 100,000 rolls**
```python
import random

NUM_ROLLS  = 100_000
NUM_SIDES  = 6

frequency = [0] * 19   # indices 3–18 used

for _ in range(NUM_ROLLS):
    d1 = random.randint(1, NUM_SIDES)
    d2 = random.randint(1, NUM_SIDES)
    d3 = random.randint(1, NUM_SIDES)
    frequency[d1 + d2 + d3] += 1

print(f"{'Sum':>5}  {'Count':>8}  {'Share':>7}  {'Expected':>10}")
print("-" * 38)
for dot_sum in range(3, 19):
    count = frequency[dot_sum]
    share = count / NUM_ROLLS
    ways  = sum(1 for a in range(1, 7)
                  for b in range(1, 7)
                  for c in range(1, 7)
                  if a + b + c == dot_sum)
    expected = ways / 216
    print(f"{dot_sum:>5}  {count:>8}  {share:>7.1%}  {expected:>10.1%}")
```

The sums 10 and 11 are the most common (27 ways each out of 216), and the simulated share will be close to the expected after 100,000 rolls. Note the triple-nested comprehension for counting ways — a good example of list comprehensions replacing nested loops.
