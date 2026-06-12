# file: ex_08_04_vector2d_start.py
import math

class Vector2D:
    def __init__(self, x, y):
        # TODO: store _x and _y
        pass

    def __str__(self):
        # TODO: return "Vector2D(x, y)"
        pass

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        # TODO: return new Vector2D with summed components
        pass

    def __sub__(self, other):
        # TODO: return new Vector2D with subtracted components
        pass

    def __mul__(self, scalar):
        # TODO: return new Vector2D scaled by scalar
        pass

    def __neg__(self):
        # TODO: return new Vector2D with negated components
        pass

    def __abs__(self):
        # TODO: return the magnitude: sqrt(x^2 + y^2)
        pass

    def __eq__(self, other):
        # TODO: equal if both components are equal
        pass

    def dot(self, other):
        # TODO: return dot product: x1*x2 + y1*y2
        pass


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
