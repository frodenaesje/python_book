# file: sc_13_07_read_only_property.py
class Circle:
    def __init__(self, radius):
        # Validate on construction; read-only afterward.
        if radius < 0 or radius > 99:
            raise ValueError(f"Invalid radius {radius}")
        self._radius = radius

    @property
    def radius(self):  # Getter for radius; read-only
        return self._radius

# Try Circle with a read-only property.
try:
    c1 = Circle(10)
    print(c1.radius)  # property getter is called
    # Setting a new radius fails: property is read-only.
    c1.radius = 20
except AttributeError as ex:
    print("AttributeError:", ex)

# Invalid construction; validation happens in __init__.
try:
    c2 = Circle(-2)
except ValueError as ex:
    print("ValueError:", ex)
