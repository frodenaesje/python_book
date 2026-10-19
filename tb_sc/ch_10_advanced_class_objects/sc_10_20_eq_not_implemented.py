# file: sc_10_20_eq_not_implemented.py
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self._x, self._y) == (other._x, other._y)


    def __hash__(self):
        return hash((self._x, self._y))
    
p1 = Point(3, 4)
print(p1 == Point(3, 4))      # True
print(p1.__eq__(Point(3, 4))) # True
print(p1.__eq__(5)) # NotImplemented - from __eq__()
print(p1 == 5)      # False - from the == operator