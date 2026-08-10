# file: ex_08_01_rectangle_start.py

class Rectangle:
    def __init__(self, width, height):
        # TODO: store _width and _height
        pass

    def area(self):
        # TODO: return the area
        pass

    def perimeter(self):
        # TODO: return the perimeter
        pass

    def is_square(self):
        # TODO: return True if width == height
        pass

    def __str__(self):
        # TODO: return e.g. "Rectangle(width=10, height=5)"
        pass

    def __eq__(self, other):
        # TODO: two rectangles are equal if they have the same area
        pass

    def __lt__(self, other):
        # TODO: a rectangle is less than another if its area is smaller
        pass

    @staticmethod
    def is_valid(width, height):
        # TODO: return True if both values are positive
        pass


if __name__ == "__main__":
    r1 = Rectangle(10, 5)
    r2 = Rectangle(6, 12)
    r3 = Rectangle(7, 7)

    print(r1)
    print(f"Area:      {r1.area()}")
    print(f"Perimeter: {r1.perimeter()}")
    print(f"Square?    {r1.is_square()}")
    print(f"Square?    {r3.is_square()}")
    print(f"r1 == r2?  {r1 == r2}")
    print(f"r1 < r2?   {r1 < r2}")
    print(f"r1 > r2?   {r1 > r2}")
