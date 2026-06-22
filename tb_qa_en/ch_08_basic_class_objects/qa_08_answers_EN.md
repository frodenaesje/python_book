# Chapter 8 – Answer Key: Review Questions

## Understanding

**1. Class vs. object**
A class is a template or blueprint — it describes what attributes and methods objects of that type should have. An object is a concrete instance of the class, with its own values for the attributes. `Car` is the class; `my_car = Car("Toyota", "Blue")` is an object.

**2. `__init__()` and when it is called**
`__init__()` is the constructor — it initialises the object's attributes and ensures the object is in a valid state from the very start. It is called automatically when we create an object, e.g. `Car("Toyota", "Blue")`.

**3. What is `self`?**
`self` is a reference to the concrete object the method is called on. Python passes it automatically as the first argument when we call an instance method — we do not write `self` ourselves in the method call.

**4. `my_car.drive()` behind the scenes**
Python rewrites `my_car.drive()` as `Car.drive(my_car)`. The class `Car` owns the code, and `my_car` is passed in as `self` so the method knows which attributes to work with.

**5. Code is shared, attributes are unique**
All objects of the same class use the same code (the methods). Attributes, however, are stored on each individual object and are unique. Two `Car` objects share the `drive()` method but each have their own `_brand` and `_color`.

**6. Convention for "private" attributes**
A leading underscore, e.g. `_balance`, is a convention meaning "internal use — do not access this directly from client code". It is an agreement between developers, not a technical barrier — Python does not prevent you from reading or changing the attribute.

**7. Name mangling**
Attribute names with a double underscore, e.g. `__balance`, are renamed internally to `_ClassName__balance`. The purpose is to avoid name conflicts in inheritance, not to create truly private attributes. It is not recommended as a replacement for `private` from C++/Java.

**8. Property and the advantage of a setter**
A property lets client code read and write an attribute using its clean name (`account1.balance`) without dealing with the internal representation. The main advantage is that the setter method can contain validation — e.g. preventing a negative balance — without the client code needing to change.

**9. Class variable vs. instance variable**
An instance variable belongs to a single object and is created with `self._name` in `__init__()`. A class variable belongs to the class and is shared by all objects — it is declared inside the class but outside all methods, e.g. `_account_count = 0`.

**10. `@classmethod` vs. `@staticmethod`**
A class method (`@classmethod`) receives the class as its first argument (`cls`) and can read and modify class variables. A static method (`@staticmethod`) receives neither `self` nor `cls` — it belongs to the class logically but needs no access to object or class data. Used for helper functions that naturally belong in the class.

**11. Dunder method and `==`**
Dunder methods are special methods with double underscores, such as `__eq__()`, `__str__()` and `__add__()`. Python calls them implicitly when operators are used. When we write `circle1 == circle2`, Python calls `circle1.__eq__(circle2)`.

**12. Object without `__bool__()`**
Python uses a fallback hierarchy: first `__bool__()` is checked, then `__len__()` (true if > 0), and finally the object is always true if neither method exists. An object without `__bool__()` is therefore always truthy.

**13. `__str__()` vs. `__repr__()`**
`__str__()` is for humans — readable output, called by `print()`. `__repr__()` is for developers — should ideally give a string that recreates the object, called by the REPL. Without `__str__()` Python falls back to `__repr__()`. Without either, `object`'s fallback prints the class name and memory address.

**14. Overloading vs. overriding**
Overloading means defining multiple versions of the same method with different parameter lists — common in Java and C++, not directly supported in Python (the second definition simply replaces the first). Overriding means replacing a method inherited from a base class with a new implementation in a subclass. What Python calls operator overloading is technically overriding: we replace inherited dunder methods from `object` to give operators new behaviour for our class.

**15. `@dataclass` and what it generates automatically**
`@dataclass` is a decorator that reads field declarations and automatically generates `__init__()`, `__repr__()` and `__eq__()`. Fields are declared with name and type directly in the class block: `x: int`. This reduces boilerplate for simple data classes that mainly store values together.

**16. Why `items: list = []` is not allowed in a `@dataclass` — and the solution**
`[]` is evaluated once when the class is defined — all instances would share the exact same list object. Changes to one instance would silently affect all others. The solution is `field(default_factory=list)`, which calls `list()` to create a fresh, independent list for each new instance.

---

## Practical

**17. `Person` with `greet()`**
```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age  = age

    def greet(self) -> None:
        print(f"Hello, my name is {self._name} and I am {self._age} years old.")

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p1.greet()
p2.greet()
```

**18. `__str__()` in `Person`**
```python
def __str__(self) -> str:
    return f"Person(name={self._name}, age={self._age})"

print(p1)   # Person(name=Alice, age=30)
```

**19. Property `age` with validation**
```python
@property
def age(self) -> int:
    return self._age

@age.setter
def age(self, value: int) -> None:
    if value < 0:
        print("Age cannot be negative!")
    else:
        self._age = value
```

**20. `my_car.drive()` vs. `Car.drive(my_car)`**
```python
my_car = Car("Toyota", "Blue")
my_car.drive()        # Toyota car is driving!
Car.drive(my_car)     # Toyota car is driving! — identical result
```

**21. `__eq__()` in `BankAccount`**
```python
class BankAccount:
    def __init__(self, balance: float) -> None:
        self._balance = balance

    def __eq__(self, other: object) -> bool:
        return self._balance == other._balance

a1 = BankAccount(1000)
a2 = BankAccount(1000)
a3 = BankAccount(500)
print(a1 == a2)   # True
print(a1 == a3)   # False
```

**22. `Playlist` with `__getitem__()`**
```python
class Playlist:
    def __init__(self) -> None:
        self._songs: list[str] = []

    def add(self, song: str) -> None:
        self._songs.append(song)

    def __getitem__(self, key):
        return self._songs[key]

pl = Playlist()
pl.add("Song A")
pl.add("Song B")
pl.add("Song C")
print(pl[0])      # Song A
print(pl[-1])     # Song C
print(pl[0:2])    # ['Song A', 'Song B']
```

**23. `__bool__()` in `Playlist`**
```python
def __bool__(self) -> bool:
    return len(self._songs) > 0

empty = Playlist()
if not empty:
    print("The playlist is empty")

pl.add("Song A")
if pl:
    print("The playlist has content")
```

**24. `@dataclass` `Point` with equality check**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(p1)           # Point(x=3, y=4)
print(p1 == p2)     # True  — __eq__() generated automatically
print(p1 == p3)     # False
```

**25. `Point` with `tags: list` using `field(default_factory=list)`**
```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    tags: list = field(default_factory=list)

p1 = Point(3, 4)
p2 = Point(3, 4)

p1.tags.append("origin")
print(p1.tags)   # ['origin']
print(p2.tags)   # []  — separate list, not shared
```
