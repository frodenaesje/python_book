# file: sc_08_15_point_dataclass.py
# Point class, implementation as a dataclass
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)
print(p1)           # Point(x=3, y=4)
print(p1 == p2)     # True
print(p1 == p3)     # False

# default_factory creates a fresh default value for each instance,
# so separate objects do not share the same mutable list.

@dataclass
class Bag:
    items: list = field(default_factory=list)


b1 = Bag()
b2 = Bag()
b1.items.append("apple")

print(b1.items)   # ['apple']
print(b2.items)   # []   - separate list, not shared
