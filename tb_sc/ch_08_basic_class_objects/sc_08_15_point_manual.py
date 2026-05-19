# file: sc_08_15_point_manual.py
# Point class, regular implementation, not as a dataclass
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point(x={self._x}, y={self._y})"

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)
print(p1)           # Point(x=3, y=4)
print(p1 == p2)     # True
print(p1 == p3)     # False
