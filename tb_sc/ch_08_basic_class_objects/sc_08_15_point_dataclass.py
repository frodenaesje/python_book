# file: sc_08_15_point_dataclass.py
# Point class, implementation as a dataclass
from dataclasses import dataclass

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
