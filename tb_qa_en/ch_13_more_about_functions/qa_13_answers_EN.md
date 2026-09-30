# Chapter 13 – Answer Key: Review Questions

## Understanding

**1. Functions as first-class objects**
Functions are first-class objects, meaning they are treated like any other value: they can be assigned to names, passed as arguments to other functions, returned from functions, and stored in lists and dictionaries. Example: `bt = tk.Button(root, command=on_click)` passes the function reference `on_click` as an argument.

**2. What is a closure?**
A closure is a function that retains access to bindings from an enclosing function scope. It can use those bindings while the enclosing function is still running or after it has returned. Returning the inner function is a common use of a closure, not a necessary condition for one to exist. A closure does not automatically copy or freeze the values of those bindings.

**3. Free variables and closure cells**
In this closure context, a free variable is a name used by the inner function but bound in an enclosing function. The inner function can retain access to that binding through a closure cell, so the binding can remain available after the enclosing function returns.

**4. `lambda` with and without call**
```python
command=on_button_click("Hello", some_list)          # Calls the function when evaluated
command=lambda: on_button_click("Hello", some_list)  # Supplies a lambda to call later
```
The first expression calls `on_button_click` immediately when the expression is evaluated and supplies its return value as `command`. The second supplies a lambda for later invocation; when Tkinter calls the lambda, its body calls `on_button_click` with the chosen arguments. Whether referenced variables participate in a closure depends on their scope: a module-level lambda that looks up `some_list` globally is not a closure merely because it refers to that name.

**5. `@add_enthusiasm`**
`@add_enthusiasm` before a function definition is shorthand for:
```python
say = add_enthusiasm(say)
```
Python runs this assignment automatically right after `say` is defined.

**6. `*args` and `**kwargs` in wrapper**
A wrapper can collect positional arguments in `*args` and keyword arguments in `**kwargs`, then explicitly forward them with `func(*args, **kwargs)`. This supports different compatible call shapes without defining a fixed parameter list. A fixed-signature wrapper is valid when it supports the calls being made, including calls to functions with additional optional parameters. Forwarding does not bypass the wrapped function's own argument validation.

**7. Closure-based decorator vs. `@property`**
A closure-based decorator takes a function as an argument, wraps it in a new function and returns the wrapper function. `@property` is a class-based decorator that creates a descriptor object — it implements the descriptor protocol with `__get__`, `__set__` and `__delete__`, and translates the dot operator into method calls.

**8. Descriptor and the three methods**
A descriptor is an object whose type implements one or more descriptor protocol methods and which is used as a class attribute to participate in attribute access. The methods discussed are:

- `__get__()` - called when we read an attribute
- `__set__()` - called when we assign to an attribute
- `__delete__()` - called when we delete an attribute

A descriptor need not implement all three methods.

**9. `self.radius` vs. `self._radius` in `__init__()`**
In the chapter's `Circle` example, `self.radius = radius` uses the public property name and invokes the setter, including its validation. `self._radius = radius` assigns the backing attribute directly and bypasses that setter. Construction could still validate the value separately before assigning the backing attribute. The underscore in `_radius` is a convention, not enforced privacy.

**10. `@property` without a setter**
A property without a setter prevents ordinary assignment through that property name; such assignment raises `AttributeError`. The exact exception message can vary. The backing attribute can still be writable, so this does not make the whole object immutable.

**11. `nonlocal` vs. `global`**
`nonlocal` makes a name refer to an existing binding in the nearest enclosing function scope that binds that name, allowing rebinding there. `global` refers to the module-level binding. Neither declaration is needed merely to read the relevant name or to mutate an object it already references. Rebinding a name, such as assigning a new value to a counter, differs from mutating an existing object, such as appending to a list.

**12. `lambda` vs. `def`**
A lambda expression creates a function whose body is one expression and whose result is returned automatically. A `def` statement defines a function with a statement suite, allowing statements such as `return` and a docstring. Both create function objects. The lambda restriction is one expression, not one physical source line: normal Python expression syntax can allow a lambda to span multiple lines.

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
