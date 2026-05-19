# Pythonic patterns – Chapter 10: More on classes and objects

## `super()` — class name vs. `super()`

| Beginner / C++/Java style | Pythonic |
|---------------------------|----------|
| `Animal.__init__(self, name)` | `super().__init__(name)` |

`super()` is more robust — if we rename the class we do not need to update all calls. Also works correctly with multiple inheritance.

## Overriding `__str__()` and reusing the superclass version

| Beginner | Pythonic |
|----------|----------|
| `def __str__(self):`<br>`    return f"Name: {self._name}, Age: {self._age}, ID: {self._student_id}"` | `def __str__(self):`<br>`    return super().__str__() + f", ID: {self._student_id}"` |

`super().__str__()` reuses the superclass implementation. The subclass does not own the superclass's attributes — it is the superclass's responsibility to display them.

## `isinstance()` vs. `type()`

| Beginner | Pythonic |
|----------|----------|
| `if type(animal) == Dog:` | `if isinstance(animal, Dog):` |

`isinstance()` returns `True` for subclasses of `Dog` too. `type() == Dog` returns `False` for subclasses.

## Abstract class vs. convention

| Beginner | Pythonic |
|----------|----------|
| `class Animal:`<br>`    def speak(self):`<br>`        raise NotImplementedError` | `from abc import ABC, abstractmethod`<br>`class Animal(ABC):`<br>`    @abstractmethod`<br>`    def speak(self): pass` |

`@abstractmethod` gives an error at *instantiation* — not at *call*. We discover the error earlier and get a clearer message.

## `__eq__()` and `__hash__()` — always together

| Beginner | Pythonic |
|----------|----------|
| `def __eq__(self, other):`<br>`    return self._x == other._x` | `def __eq__(self, other):`<br>`    return self._x == other._x`<br><br>`def __hash__(self):`<br>`    return hash((self._x,))` |

If we override `__eq__()` without `__hash__()` the object becomes unhashable. The two always go together.

## `__repr__()` as a developer tool

| Beginner | Pythonic |
|----------|----------|
| Implements only `__str__()` | Implements both `__str__()` and `__repr__()` |
| `def __str__(self):`<br>`    return f"Point({self._x}, {self._y})"` | `def __str__(self):`<br>`    return f"({self._x}, {self._y})"`<br><br>`def __repr__(self):`<br>`    return f"Point({self._x}, {self._y})"` |

`__str__()` is for the end user; `__repr__()` is for the developer. The REPL uses `__repr__()` — without it we only see a memory address.

## Iterable collection — delegating vs. implementing from scratch

| Beginner | Pythonic |
|----------|----------|
| `def __iter__(self):`<br>`    self._index = 0`<br>`    return self`<br><br>`def __next__(self):`<br>`    if self._index < len(self._data):`<br>`        ...` | `def __iter__(self):`<br>`    return iter(self._data)` |

Delegating to `iter(self._data)` is shorter, safer and returns a new iterator on each call. Use a separate iterator class only when you need filtering or transformation along the way.

## Composition vs. aggregation — who creates?

| Composition | Aggregation |
|-------------|-------------|
| `def add_line(self, product, qty, price):`<br>`    self._lines.append(OrderLine(product, qty, price))` | `def add_member(self, person):`<br>`    self._members.append(person)` |

Composition: the whole creates the parts itself — client code never sees them. Aggregation: the parts are created outside and passed in. Same syntax, different design choice.

## Generator vs. iterator class

| Beginner | Pythonic |
|----------|----------|
| `class CountUp:`<br>`    def __init__(self, start, stop):`<br>`        self._current = start`<br>`        self._stop = stop`<br>`    def __iter__(self): return self`<br>`    def __next__(self):`<br>`        if self._current >= self._stop:`<br>`            raise StopIteration`<br>`        value = self._current`<br>`        self._current += 1`<br>`        return value` | `def count_up(start, stop):`<br>`    current = start`<br>`    while current < stop:`<br>`        yield current`<br>`        current += 1` |

The generator function is shorter, easier to read, and Python handles `__iter__()`, `__next__()` and `StopIteration` automatically. Use an iterator class only when you need shared state between multiple methods.

## Generator expression vs. list comprehension

| Beginner | Pythonic |
|----------|----------|
| `squares = [x**2 for x in range(1_000_000)]` | `squares = (x**2 for x in range(1_000_000))` |

A list comprehension builds the entire list in memory immediately. A generator expression is lazy — it computes one value at a time. For large datasets the memory difference is significant.
