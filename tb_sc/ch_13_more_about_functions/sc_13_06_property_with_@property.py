# file: sc_13_06_property_with_@property.py
# Circle class with @property decorator
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):  # Getter for radius
        return self._radius

    @radius.setter  # Setter for radius
    def radius(self, radius):
        if radius < 0 or radius > 99:
            raise ValueError(f"Invalid radius {radius}")
        self._radius = radius

# Try Circle
try:
    c1 = Circle(10)
    print(c1.radius)  # property getter is called
    c1.radius = 20  # property setter is called
    c1.radius = -2  # property setter raises ValueError
except ValueError as ex:
    print("Exception: ",ex)
