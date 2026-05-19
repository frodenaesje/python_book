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

Without `i=i` all lambda functions remember the same variable `i` — and use the last value when called. With `i=i` the value is captured at creation time.

## Decorator — manual vs. `@`-syntax

| Beginner | Pythonic |
|----------|----------|
| `def say(name): ...`<br>`say = add_enthusiasm(say)` | `@add_enthusiasm`<br>`def say(name): ...` |

The `@`-syntax makes it explicit that the function is decorated — and places that information where it belongs: right next to the definition.

## Wrapper with fixed vs. flexible signature

| Beginner | Pythonic |
|----------|----------|
| `def wrapper(data):`<br>`    return func(data)` | `def wrapper(*args, **kwargs):`<br>`    return func(*args, **kwargs)` |

A fixed signature limits the decorator to functions with exactly one argument. `*args`/`**kwargs` makes it general and reusable.

## `@property` vs. direct attribute access

| Beginner | Pythonic |
|----------|----------|
| `def set_radius(self, r):`<br>`    self._radius = r`<br>`def get_radius(self):`<br>`    return self._radius` | `@property`<br>`def radius(self):`<br>`    return self._radius`<br>`@radius.setter`<br>`def radius(self, r):`<br>`    self._radius = r` |

`@property` gives the user clean dot-syntax (`c.radius`) while we retain control over validation and logic.

## Read-only attribute

| Beginner | Pythonic |
|----------|----------|
| `# Comment: do not set this directly`<br>`self._radius = radius` | `@property`<br>`def radius(self):`<br>`    return self._radius`<br>`# No setter = read-only` |

Without a setter any attempt to assign raises `AttributeError` — not just a convention that can be broken.

## `property()` vs. `@property`

| Beginner | Pythonic |
|----------|----------|
| `def _get_r(self): return self._r`<br>`def _set_r(self, v): self._r = v`<br>`radius = property(_get_r, _set_r)` | `@property`<br>`def radius(self): return self._r`<br>`@radius.setter`<br>`def radius(self, v): self._r = v` |

The `@property` syntax is more readable and keeps the getter and setter visually close together with named methods.
