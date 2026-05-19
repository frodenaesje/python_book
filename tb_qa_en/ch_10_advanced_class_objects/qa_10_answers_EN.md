# Chapter 10 – Answer Key: Review Questions

## Understanding

**1. is-a vs. has-a**
is-a is inheritance — a subclass *is a* variant of the superclass. `Dog` is an `Animal`. has-a is composition or aggregation — one object *contains* another. `Order` has `OrderLine` objects.

**2. The diamond in UML**
The diamond indicates that one class owns or contains objects of another class. A filled diamond means composition — the parts cannot exist without the whole. An open diamond means aggregation — the parts can exist independently.

**3. What a subclass inherits**
The subclass inherits all attributes and methods from the superclass. It adds its own attributes in its `__init__()` and can override methods from the superclass with a new implementation.

**4. `super().__init__()` and the consequence of omitting it**
`super().__init__()` calls the constructor in the superclass and ensures that the superclass's attributes are created on the object. If we omit it, the superclass's attributes are never created — we get `AttributeError` the first time we try to use them.

**5. Polymorphism and its variants**
Polymorphism means that objects of different classes can be treated the same way but behave differently. Via inheritance: subclasses override methods from the superclass. Via duck typing: objects without a common superclass but with the same method name — Python does not care about the type, only that the method exists.

**6. `isinstance()`**
`isinstance(obj, Class)` returns `True` if `obj` is an instance of `Class` or a subclass of it. It is safer than `type(obj) == Class`, which only returns `True` for exactly that class — not subclasses.

**7. Abstract class**
An abstract class cannot be instantiated directly — if we try we get a `TypeError`. It defines a contract: all subclasses *must* implement the abstract methods. A subclass that does not implement all of them cannot be instantiated either.

**8. Composition vs. aggregation — syntactically different in Python?**
Composition: the whole creates the parts itself inside its own methods — client code never sees them directly. Aggregation: the parts are created outside and passed in as references. Both are implemented in Python by having one object hold references to others — it is a design choice, not a syntactic difference.

**9. `__str__()` vs. `__repr__()`**
`__str__()` is for humans — readable output, called by `print()`. `__repr__()` is for developers — should ideally give a string that recreates the object, called by the REPL. Without `__str__()` Python falls back to `__repr__()`. Without either, `object`'s fallback prints the class and memory address.

**10. `object`'s default `__eq__()`**
`object`'s `__eq__()` compares identity — two variables are equal only if they point to exactly the same object in memory. We must override it if we want two objects with the same content to be considered equal.

**11. `__hash__()` when we override `__eq__()`**
Python automatically sets the `__hash__` method to `None`. This means `hash(obj)` raises a `TypeError`, and the object can no longer be used as a dictionary key or in a set.

**12. The rule for `__eq__()` and `__hash__()`**
If `a == b` is `True`, then `hash(a) == hash(b)` must also be `True`. The reverse does not necessarily hold — two different objects can coincidentally get the same hash (a hash collision). If we override `__eq__()` we must therefore always override `__hash__()` to uphold the rule.

**13. Iterable vs. iterator**
An iterable is an object we can iterate over — it implements `__iter__()` which returns an iterator. An iterator is an object that keeps track of where we are in the traversal — it implements `__next__()` and raises `StopIteration` when there are no more elements. An iterator is always itself an iterable.

**14. Behind the scenes in the for loop**
First `iter(iterable)` is called, which calls `iterable.__iter__()` — this returns an iterator object. Then `next(iterator)` is called repeatedly, which calls `iterator.__next__()` for each element. When `StopIteration` is raised the loop ends.

**15. A list can be reused; an iterator cannot**
`iter(lista)` creates a *new* iterator on each call — the list is unchanged and can be reused in new loops. An iterator remembers where it is via an internal index and cannot be rewound — after all elements have been retrieved it is exhausted.

**16. What is a generator?**
A generator is a function that uses `yield` instead of `return`. It does not return one value and terminate — it pauses itself, delivers one value and remembers exactly where it left off. The next time `next()` is called it continues from there. Python automatically creates a generator object that implements the iterator protocol — we do not need to write `__iter__()` and `__next__()` ourselves.

**17. `yield` vs. `return`**
`return` terminates the function and sends a value back. The next time the function is called it starts from the beginning — all local state is gone. `yield` pauses the function and sends a value back but preserves the entire state: local variables, which line we are on, everything. The next time `next()` is called the function continues from where it left off.

**18. Generator expression vs. list comprehension**
A list comprehension `[x**2 for x in range(n)]` computes all values at once and stores them in a list in memory. A generator expression `(x**2 for x in range(n))` is lazy — it computes one value at a time when requested. For large datasets a generator expression is significantly more memory-efficient since it never stores the entire result at once.

---

## Practical

**19. `Shape` with subclasses**
```python
class Shape:
    def area(self) -> float:
        return 0.0

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width  = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return 3.14159 * self._radius ** 2

shapes: list[Shape] = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")
```

**20. `__str__()` and `__repr__()`**
```python
class Shape:
    def __str__(self) -> str:
        return f"{self.__class__.__name__} with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width  = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def __repr__(self) -> str:
        return f"Rectangle({self._width}, {self._height})"

r = Rectangle(4, 5)
print(r)       # Rectangle with area 20.00  — uses __str__()
print(repr(r)) # Rectangle(4, 5)            — uses __repr__()
```

**21. Abstract `Shape`**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

shape = Shape()   # TypeError: Can't instantiate abstract class Shape
```

**22. `Playlist` with `__iter__()`**
```python
class Song:
    def __init__(self, title: str) -> None:
        self._title = title

    def __str__(self) -> str:
        return self._title

class Playlist:
    def __init__(self) -> None:
        self._songs: list[Song] = []

    def add(self, song: Song) -> None:
        self._songs.append(song)

    def __iter__(self):
        return iter(self._songs)

s1 = Song("Bohemian Rhapsody")
s2 = Song("Hotel California")
pl = Playlist()
pl.add(s1)
pl.add(s2)
for song in pl:
    print(song)
```

**23. REPL — iterator exhaustion**
```python
lista = [1, 2, 3]
it = iter(lista)
print(next(it))    # 1 — iterator is now at position 1
print(next(it))    # 2 — iterator is now at position 2
for x in lista:
    print(x)       # 1 2 3 — new iterator each time; list is unchanged
for x in it:
    print(x)       # 3 — iterator is at position 2, only one element left
```
The last loop prints only 3 — the iterator `it` remembers that it has already retrieved 1 and 2.

**24. `Color` with `__eq__()` and `__hash__()`**
```python
class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._r = r
        self._g = g
        self._b = b

    def __eq__(self, other: object) -> bool:
        return self._r == other._r and self._g == other._g and self._b == other._b

    def __hash__(self) -> int:
        return hash((self._r, self._g, self._b))

red1 = Color(255, 0, 0)
red2 = Color(255, 0, 0)
print(red1 == red2)              # True
print(hash(red1) == hash(red2))  # True

lookup = {red1: "red"}
print(lookup[red2])              # red — works because hashes are equal
```

**25. Generator `even_numbers`**
```python
def even_numbers(limit: int):
    current = 0
    while current < limit:
        yield current
        current += 2

for n in even_numbers(10):
    print(n, end=" ")       # 0 2 4 6 8

print(list(even_numbers(10)))   # [0, 2, 4, 6, 8]
```

**26. `CountUp` rewritten as a generator**
```python
# Class-based (15 lines):
class CountUp:
    def __init__(self, start: int, stop: int) -> None:
        self._current = start
        self._stop    = stop

    def __next__(self) -> int:
        if self._current >= self._stop:
            raise StopIteration
        value = self._current
        self._current += 1
        return value

    def __iter__(self):
        return self

# As a generator (5 lines):
def count_up(start: int, stop: int):
    current = start
    while current < stop:
        yield current
        current += 1

for n in count_up(1, 5):
    print(n, end=" ")   # 1 2 3 4
```

Python handles `__iter__()`, `__next__()` and `StopIteration` automatically for the generator. We do not need to manage index and state ourselves — `yield` takes care of it.
