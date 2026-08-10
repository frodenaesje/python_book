# file: ex_10_01_geo_objects_start.py
import math
from abc import ABC, abstractmethod


class GeoObject(ABC):
    def __init__(self, fill_color="none", line_color="black"):
        # TODO: store _fill_color and _line_color
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        # TODO: return e.g. "Circle        area=  78.54  perimeter=  31.42  fill=red"
        # Hint: use type(self).__name__ to get the class name
        pass


class Circle(GeoObject):
    def __init__(self, radius, fill_color="none", line_color="black"):
        # TODO: call super().__init__() and store _radius
        pass

    @property
    def radius(self):
        # TODO: return _radius
        pass

    @radius.setter
    def radius(self, value):
        # TODO: validate positive, raise ValueError otherwise
        pass

    def area(self):
        # TODO: pi * r^2
        pass

    def perimeter(self):
        # TODO: 2 * pi * r
        pass


class Rectangle(GeoObject):
    def __init__(self, width, height, fill_color="none", line_color="black"):
        # TODO: call super().__init__() and store _width, _height
        pass

    @property
    def width(self):
        pass

    @width.setter
    def width(self, value):
        # TODO: validate positive
        pass

    @property
    def height(self):
        pass

    @height.setter
    def height(self, value):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


if __name__ == "__main__":
    shapes = [
        Circle(5, fill_color="red"),
        Rectangle(4, 6),
        Circle(7),
        Rectangle(10, 5, fill_color="blue"),
    ]

    for s in shapes:
        print(s)

    largest = max(shapes, key=lambda s: s.area())
    print(f"\nLargest area: {largest}")
