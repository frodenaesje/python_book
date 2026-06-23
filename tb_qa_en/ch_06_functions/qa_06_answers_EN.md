# Chapter 6 – Answer Key: Review Questions

## Understanding

**1. Mandatory parts of a function header**
`def`, function name, parentheses `()` and colon `:`. Parameters are optional.

**2. Argument vs. parameter**
A parameter is the variable name inside the function definition. An argument is the value passed in when the function is called.

**3. Function without `return`**
Returns `None` automatically. The same applies if `return` is used without a value.

**4. Docstring**
A text string that documents what a function does, placed as the first line of the function block enclosed in triple quotes. Read in REPL with `help(function_name)`.

**5. Changing `int` or `str` inside a function**
`int` and `str` are immutable — they cannot be changed. An assignment like `x = x + 1` inside the function creates a new object with a new id. The original outside the function is unchanged, which an `id()` comparison confirms.

**6. Calling `append()` on a list passed as an argument**
The list is mutable, and the reference is copied — not the object. `append()` modifies the same list object that the call site refers to. The change is visible outside the function, and `id()` is unchanged.

**7. Keyword arguments**
Allow arguments to be passed by name, in any order. Makes the code more readable, especially when there are many parameters.

**8. Mutable object as default value**
Default values are evaluated only once when the function is defined. A mutable object like `[]` will be shared between all calls that do not pass in their own argument — changes accumulate. The solution is to use `None` as the default value and create the object inside the function.

**9. `*args` vs. `**kwargs`**
`*args` collects an arbitrary number of positional arguments into a tuple. `**kwargs` collects an arbitrary number of keyword arguments into a dictionary.

**10. LEGB**
Local → Enclosing → Global → Built-in. The order in which Python searches for a variable name.

**11. `for` and `if` do not create their own scope**
Unlike e.g. Java and C++, variables defined inside `for`, `while`, `if` and `try` blocks live on in the enclosing scope after the block finishes. Only `def`, `class`, comprehensions and `lambda` create their own scope.

**12. `if __name__ == "__main__":`**
When a file is run directly, `__name__` is set to `"__main__"`. When the file is imported as a module, `__name__` is set to the module name. This construct ensures that test code only runs on direct execution, not on import.

**13. `sys.argv` and `sys.argv[0]`**
`sys.argv` is a list Python fills with command-line arguments when a script is started. `sys.argv[0]` is always the filename of the script itself. `sys.argv[1]` is the first argument the user passed in. All elements are strings.

**14. `*args` vs. `sys.argv`**
`*args` collects arguments from the code that calls the function — a Python mechanism inside the program. `sys.argv` collects arguments from the user who starts the script in the terminal — a mechanism between the operating system and the program. Both give access to a variable number of values, but from completely different sources.

**15. `Optional[str]` and modern syntax**
`Optional[str]` means the value is either a `str` or `None` — imported from the `typing` module. The modern equivalent from Python 3.10 is `str | None`, which requires no import. Both express the same thing.

**16. `list` vs. `list[int]` as a type hint**
`list` only says that the value is a list — nothing about its contents. `list[int]` is more precise: a list where all elements are integers. IDEs use this information for better autocompletion and type warnings.

**17. `sys.exit(1)`**
`sys.exit()` terminates the program immediately. The argument is an exit code sent to the operating system. `0` means "ended normally". Any other number — typically `1` — means "something went wrong". Shell scripts and other programs can read this code.

---

## Practical

**18. `square(n)` with type hints and docstring**
```python
def square(n: int) -> int:
    """Returns the square of n."""
    return n * n

print(square(3))   # 9
print(square(10))  # 100
```

**19. `greet` with default value**
```python
def greet(name: str, greeting: str = "Hello") -> None:
    print(f"{greeting}, {name}!")

greet("Anna")           # Hello, Anna!
greet("Jon", "Hi")      # Hi, Jon!
```

**20. `min_max`**
```python
def min_max(lst: list[int]) -> tuple[int, int]:
    """Returns the smallest and largest value in the list."""
    return min(lst), max(lst)

lowest, highest = min_max([3, 7, 1, 9, 4])
print(lowest)    # 1
print(highest)   # 9
```

**21. `count_above`**
```python
def count_above(lst: list[int], threshold: int) -> int:
    """Returns the number of elements greater than threshold."""
    count = 0
    for element in lst:
        if element > threshold:
            count += 1
    return count

print(count_above([3, 7, 1, 9, 4], 5))  # 2
```
`count` is a local variable — changes do not affect anything outside the function.

**22. `double_all` in place**
```python
def double_all(lst: list[int]) -> None:
    """Doubles each element in the list in place."""
    for i in range(len(lst)):
        lst[i] *= 2

numbers = [1, 2, 3, 4, 5]
double_all(numbers)
print(numbers)  # [2, 4, 6, 8, 10] — the original is changed!
```

**23. `sum_all` with `*args`**
```python
def sum_all(*numbers: int) -> int:
    """Sums an arbitrary number of integers."""
    return sum(numbers)

print(sum_all(1, 2, 3))    # 6
nums = [10, 20, 30]
print(sum_all(*nums))       # 60
```

**24. Script with `sys.argv`**
```python
import sys

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(f"Opening: {filename}")
```
Run without argument: prints the usage message and exits with code 1.
Run with argument: prints the filename.

**25. `multiply` with type hints**
```python
def multiply(numbers: list[int], factor: int) -> list[int]:
    """Returns a new list where each element is multiplied by factor."""
    return [n * factor for n in numbers]

print(multiply([1, 2, 3, 4], 3))  # [3, 6, 9, 12]
```

**26. Function returning multiple values**
```python
def min_max_avg(numbers: list[float]) -> tuple[float, float, float]:
    """Returns the minimum, maximum and average of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lowest, highest, average = min_max_avg([3.0, 7.0, 1.0, 9.0, 4.0])
print(f"Min: {lowest}, Max: {highest}, Avg: {average:.1f}")
# Min: 1.0, Max: 9.0, Avg: 4.8
```
Python packs multiple return values into a tuple automatically. At the call site we unpack the tuple into separate variables with `lowest, highest, average = ...`.
