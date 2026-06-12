# file: ex_08_04_vector2d.py
import math

class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Vector2D({self._x}, {self._y})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Vector2D(self._x - other._x, self._y - other._y)

    def __mul__(self, scalar):
        return Vector2D(self._x * scalar, self._y * scalar)

    def __neg__(self):
        return Vector2D(-self._x, -self._y)

    def __abs__(self):
        return math.sqrt(self._x**2 + self._y**2)

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def dot(self, other):
        return self._x * other._x + self._y * other._y


if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1:          {v1}")
    print(f"v2:          {v2}")
    print(f"v1 + v2:     {v1 + v2}")
    print(f"v1 - v2:     {v1 - v2}")
    print(f"v1 * 3:      {v1 * 3}")
    print(f"-v1:         {-v1}")
    print(f"|v1|:        {abs(v1)}")
    print(f"v1.dot(v2):  {v1.dot(v2)}")
    print(f"v1 == v2:    {v1 == v2}")
