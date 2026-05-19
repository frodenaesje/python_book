# Pythonic patterns – Chapter 6: Functions

## Return value from function without `return`

| Beginner | Pythonic |
|----------|----------|
| `def say_hello(name):`<br>`    print(f"Hello, {name}!")`<br>`    return None` | `def say_hello(name):`<br>`    print(f"Hello, {name}!")` |

`return None` is unnecessary — Python returns `None` implicitly.

## Docstring

| Beginner | Pythonic |
|----------|----------|
| `# Returns the square of n`<br>`def square(n):` | `def square(n):`<br>`    """Returns the square of n."""` |

Docstrings are the recommended way to document functions. Comments above the function are not accessible via `help()`.

## Returning multiple values

| Beginner | Pythonic |
|----------|----------|
| `result = []`<br>`result.append(min(lst))`<br>`result.append(max(lst))`<br>`return result` | `return min(lst), max(lst)` |

Python automatically packs multiple return values into a tuple. No list needed.

## Unpacking return values

| Beginner | Pythonic |
|----------|----------|
| `result = min_max(lst)`<br>`lowest = result[0]`<br>`highest = result[1]` | `lowest, highest = min_max(lst)` |

Unpacking at the call site is cleaner and more readable than indexing.

## Default value — mutable object

| Beginner | Pythonic |
|----------|----------|
| `def add_to(element, lst=[]):`<br>`    lst.append(element)`<br>`    return lst` | `def add_to(element, lst=None):`<br>`    if lst is None:`<br>`        lst = []`<br>`    lst.append(element)`<br>`    return lst` |

Mutable default values are shared between all calls. Use `None` and create the object inside the function.

## Summing a sequence

| Beginner | Pythonic |
|----------|----------|
| `def sum_all(*numbers):`<br>`    total = 0`<br>`    for n in numbers:`<br>`        total += n`<br>`    return total` | `def sum_all(*numbers):`<br>`    return sum(numbers)` |

The built-in `sum()` accepts an iterable — including a tuple from `*args`.

## Avoid `global`

| Beginner | Pythonic |
|----------|----------|
| `x = 0`<br>`def increment():`<br>`    global x`<br>`    x += 1` | `def increment(x):`<br>`    return x + 1`<br>`x = increment(x)` |

`global` creates hidden dependencies and makes code harder to test. Pass the value in and return the result.

## Type hints

| Beginner | Pythonic |
|----------|----------|
| `def add(a, b):`<br>`    return a + b` | `def add(a: int, b: int) -> int:`<br>`    return a + b` |

Type hints are not required, but make the intent clear and provide better IDE support.

## Keyword arguments with many parameters

| Beginner | Pythonic |
|----------|----------|
| `create_greeting("Ola", "Hello")` | `create_greeting(name="Ola", greeting="Hello")` |

Keyword arguments make the call self-documenting, especially useful when the order is not obvious.

## Command-line arguments — check count

| Beginner | Pythonic |
|----------|----------|
| `if sys.argv[1]:` | `if len(sys.argv) < 2:`<br>`    print("Missing argument")`<br>`    sys.exit(1)` |

`sys.argv[1]` raises `IndexError` if the argument is missing. Always check `len(sys.argv)` before indexing.

## Command-line arguments — type conversion

| Beginner | Pythonic |
|----------|----------|
| `age = sys.argv[1]`<br>`if age > 18:  # TypeError` | `age = int(sys.argv[1])` |

All elements in `sys.argv` are strings. Convert explicitly to the correct type.

## Compound type hints — modern syntax

| Older (`typing` module) | Pythonic (Python 3.10+) |
|-------------------------|------------------------|
| `from typing import Optional`<br>`def f(x: Optional[str]) -> Optional[int]:` | `def f(x: str \| None) -> int \| None:` |
| `from typing import Union`<br>`def f(x: Union[int, float]) -> str:` | `def f(x: int \| float) -> str:` |
| `from typing import List, Dict`<br>`def f(data: List[int]) -> Dict[str, int]:` | `def f(data: list[int]) -> dict[str, int]:` |

Python 3.9+ supports `list[int]` and `dict[str, int]` directly. Python 3.10+ supports `|` for union and Optional. No import needed.
