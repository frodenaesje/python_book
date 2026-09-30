# Pythonic patterns – Chapter 13: Advanced functions

## Passing functions as arguments

| Beginner | Pythonic |
|----------|----------|
| `def on_click(): ...`<br>`button.config(command=on_click())` | `def on_click(): ...`<br>`button.config(command=on_click)` |

With parentheses the function is called immediately and its return value is passed as `command`. Without parentheses the reference is passed — so Tkinter can call it later.

## Closure vs. global variable

| Beginner | Pythonic |
|----------|----------|
| `count = 0`<br>`def increment():`<br>`    global count`<br>`    count += 1` | `def make_counter():`<br>`    count = 0`<br>`    def increment():`<br>`        nonlocal count`<br>`        count += 1`<br>`    return increment` |

A closure keeps state encapsulated without polluting the global namespace.

## Lambda as closure vs. hardcoded value

| Beginner | Pythonic |
|----------|----------|
| `for i in range(3):`<br>`    btn = Button(command=lambda: print(i))` | `for i in range(3):`<br>`    btn = Button(command=lambda i=i: print(i))` |

When these callbacks run after the loop, the first form looks up `i` at call time and uses its final binding. At module level this is global lookup; inside an enclosing function it can use a closure cell. In `lambda i=i: ...`, the default argument is evaluated when the lambda is created, storing the current object as a default argument. This does not copy arbitrary mutable objects and is not a special kind of closure over `i`.

## Decorator — manual vs. `@`-syntax

| Beginner | Pythonic |
|----------|----------|
| `def say(name): ...`<br>`say = add_enthusiasm(say)` | `@add_enthusiasm`<br>`def say(name): ...` |

The `@`-syntax makes it explicit that the function is decorated — and places that information where it belongs: right next to the definition.

## Wrapper with fixed vs. flexible signature

| Beginner | Pythonic |
|----------|----------|
| `def wrapper(data):`<br>`    return func(data)` | `def wrapper(*args, **kwargs):`<br>`    return func(*args, **kwargs)` |

`wrapper(data)` accepts one argument and calls `func(data)`. It can wrap any function that accepts that call, including one with additional optional parameters. `*args` and `**kwargs` allow the wrapper to accept and forward more call shapes. The wrapped function still validates the supplied arguments.

## `@property` vs. direct attribute access

| Beginner | Pythonic |
|----------|----------|
| `def set_radius(self, r):`<br>`    self._radius = r`<br>`def get_radius(self):`<br>`    return self._radius` | `@property`<br>`def radius(self):`<br>`    return self._radius`<br>`@radius.setter`<br>`def radius(self, r):`<br>`    self._radius = r` |

`@property` gives the user clean dot-syntax (`c.radius`) while we retain control over validation and logic.

## Read-only attribute

| Beginner | Pythonic |
|----------|----------|
| `# Comment: do not set this directly`<br>`self._radius = radius` | `@property`<br>`def radius(self):`<br>`    return self._radius`<br>`# No setter = read-only` |

Without a setter, ordinary assignment to the property name raises `AttributeError`. The backing attribute can still be writable; this does not make the object immutable.

## `property()` vs. `@property`

| Beginner | Pythonic |
|----------|----------|
| `def _get_r(self): return self._r`<br>`def _set_r(self, v): self._r = v`<br>`radius = property(_get_r, _set_r)` | `@property`<br>`def radius(self): return self._r`<br>`@radius.setter`<br>`def radius(self, v): self._r = v` |

The `@property` syntax is more readable and keeps the getter and setter visually close together with named methods.
