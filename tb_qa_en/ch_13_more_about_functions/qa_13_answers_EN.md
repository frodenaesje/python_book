# Chapter 13 – Answer Key: Review Questions

## Understanding

**1. Functions as first-class objects**
Functions are first-class objects, meaning they are treated like any other value: they can be passed as arguments to other functions, returned from functions, and stored in variables, lists and dictionaries. Example: `bt = tk.Button(root, command=on_click)` passes the function reference `on_click` as an argument.

**2. What is a closure?**
A closure arises when an inner function refers to variables or parameters from an outer function, and the inner function lives on after the outer function has finished. The inner function "remembers" the values from the enclosing scope.

**3. Free variable and the heap**
A free variable is a variable that is used in an inner function but defined in an outer function. It cannot live on the stack because the outer function's stack frame disappears when it returns. Python instead places it in a cell object on the heap, which lives on as long as the closure function exists.

**4. `lambda` with and without call**
```python
command=on_button_click("Hello", some_list)          # Calls the function immediately at startup
command=lambda: on_button_click("Hello", some_list)  # Sends a reference — called on button press
```
The first variant runs the function immediately and sets `command` to the return value. The second creates a closure that is called when the event occurs.

**5. `@add_enthusiasm`**
`@add_enthusiasm` before a function definition is shorthand for:
```python
say = add_enthusiasm(say)
```
Python runs this assignment automatically right after `say` is defined.

**6. `*args` and `**kwargs` in wrapper**
`*args` and `**kwargs` make the wrapper function general so that it forwards all arguments to the original function regardless of its signature. Without them the wrapper would only work for functions with exactly the signature the wrapper itself defines.

**7. Closure-based decorator vs. `@property`**
A closure-based decorator takes a function as an argument, wraps it in a new function and returns the wrapper function. `@property` is a class-based decorator that creates a descriptor object — it implements the descriptor protocol with `__get__`, `__set__` and `__delete__`, and translates the dot operator into method calls.

**8. Descriptor and the three methods**
A descriptor is a design pattern for controlling attribute access. The descriptor protocol consists of:
- `__get__()` — called when we read an attribute
- `__set__()` — called when we write to an attribute
- `__delete__()` — called when we delete an attribute

**9. `self.radius` vs. `self._radius` in `__init__()`**
`self.radius = radius` goes through the property setter and activates validation. `self._radius = radius` writes directly to the private attribute and bypasses the setter — no validation happens at construction.

**10. `@property` without a setter**
The attribute becomes read-only. An attempt to assign raises `AttributeError: can't set attribute`.

**11. `nonlocal` vs. `global`**
`nonlocal` is used in closures to change a variable in the nearest enclosing function scope. `global` is used to change a variable at module level. Both are necessary because Python would otherwise interpret an assignment inside a function as the definition of a new local variable.

**12. `lambda` vs. `def`**
A lambda is syntactic sugar for an anonymous function on one line without a `return` statement — the return value is the expression after the colon. A `def` function can have multiple lines, `return` statements, docstrings and a name. Functionally they are equivalent — `type(lambda x: x)` gives `<class 'function'>`.

---

## Practical exercises

**13. `make_multiplier`**
```python
def make_multiplier(n: int):
    def multiplier(x: int) -> int:
        return x * n
    return multiplier

double   = make_multiplier(2)
triple   = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```
`multiplier` is a closure that remembers `n` from `make_multiplier()`.

**14. `@log` decorator**
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log
def add(a: int, b: int) -> int:
    return a + b

add(3, 4)
# Calling add with args=(3, 4), kwargs={}
# add returned: 7
```

**15. `Temperature` with properties**
```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius   # uses the setter

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError(f"Temperature {value} is below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:   # read-only — no setter
        return self._celsius * 9 / 5 + 32

t = Temperature(100)
print(t.celsius)    # 100
print(t.fahrenheit) # 212.0

t.celsius = -300    # ValueError
```
