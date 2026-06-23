# Pythonic Patterns - Chapter 5: Lists and the `for` Loop

## Empty list

| Novice | Pythonic |
|--------|----------|
| `list()` | `[]` |

Both are correct, but `[]` is shorter and more idiomatic when creating an empty list.

## Copying a list

| Novice | Pythonic |
|--------|----------|
| `list2 = list1` (believes this creates a copy) | `list2 = list1.copy()` |
| `list2 = list1[:]` | `list2 = list1.copy()` |

`list.copy()` is the clearest and most direct way to create a shallow copy of a list.

## Iteration - read only

| Novice | Pythonic |
|--------|----------|
| `for i in range(len(numbers)): print(numbers[i])` | `for number in numbers: print(number)` |

Direct iteration is more readable when the index is not needed.

## Iteration - modifying a list

| Novice | Pythonic |
|--------|----------|
| `for i in range(len(numbers)): numbers[i] = numbers[i] * 2` | `for i, value in enumerate(numbers): numbers[i] = value * 2` |

`enumerate()` provides both the index and the value without requiring a separate lookup.

## Sorting

| Novice | Pythonic |
|--------|----------|
| `sorted_list = list(numbers); sorted_list.sort()` | `sorted_list = sorted(numbers)` |
| `numbers.sort(); original = numbers` (incorrect - `sort()` modifies the original list) | Use `sorted()` when you want to preserve the original list. |

## List comprehension

| Novice | Pythonic |
|--------|----------|
| `squares = []`<br>`for x in range(10):`<br>`    squares.append(x * x)` | `squares = [x * x for x in range(10)]` |
| `evens = []`<br>`for x in range(21):`<br>`    if x % 2 == 0:`<br>`        evens.append(x)` | `evens = [x for x in range(21) if x % 2 == 0]` |

## Reversing a list

| Novice | Pythonic |
|--------|----------|
| `reversed_list = list(reversed(numbers))` | `reversed_list = numbers[::-1]` |

`[::-1]` is the classic Python idiom for reversing a sequence.

## Building a string from a list

| Novice | Pythonic |
|--------|----------|
| `result = ""`<br>`for s in strings:`<br>`    result += s + ", "` | `result = ", ".join(strings)` |
| `", ".join([str(n) for n in numbers])` | `", ".join(map(str, numbers))` |

`join()` is the preferred way to build strings from a list. `map()` is a concise alternative to a list comprehension for simple conversions.

## `range()` with `len()`

| Novice | Pythonic |
|--------|----------|
| `for i in range(0, len(items), 1):` | `for i in range(len(items)):` |

There is no need to specify the default start value (`0`) or step (`1`).

## `while` input loop

| Novice | Pythonic |
|--------|----------|
| `text = input("> ")`<br>`while text != "quit":`<br>`    print(text)`<br>`    text = input("> ")` | `while True:`<br>`    text = input("> ")`<br>`    if text == "quit":`<br>`        break`<br>`    print(text)` |

The novice version duplicates the `input()` call. `while True` with `break` is the preferred pattern when the termination condition depends on the value just read.

## `map()` and `filter()` vs. list comprehensions

| Novice | Pythonic |
|--------|----------|
| `list(map(lambda x: x**2, numbers))` | `[x**2 for x in numbers]` |
| `list(filter(lambda x: x > 0, numbers))` | `[x for x in numbers if x > 0]` |

List comprehensions are generally easier to read. `map()` and `filter()` remain useful when an existing function can be passed directly instead of using a `lambda`.

## `zip()` for combining two lists

| Novice | Pythonic |
|--------|----------|
| `d = {}`<br>`for i in range(len(keys)):`<br>`    d[keys[i]] = values[i]` | `d = dict(zip(keys, values))` |

`zip()` combines the two lists into pairs, and `dict()` creates the dictionary.

## `del` vs. `pop()`

| Novice | Pythonic |
|--------|----------|
| `element = items[2]; items.remove(element)` | `del items[2]` |

`del items[i]` removes an element directly by index. Use `pop(i)` if you also need the removed value.