# file: sc_13_05_property_basic.py
# Circle class with property, but no @property decorator
class Circle:
    def __init__(self, radius):
        # setter called, creates _radius attribute
        self.radius = radius
    
    def _set_radius(self, radius):  # Setter for radius
        if radius < 0 or radius > 99:
            raise ValueError(f'Invalid radius {radius}')
        self._radius = radius  # Create _radius attribute
    
    def _get_radius(self):  # Getter for radius
        return self._radius

    # create property object, radius is the name of
    # the property,
    # _get_radius is the getter method,
    # _set_radius is the setter method
    radius = property(_get_radius, _set_radius)

# Try Circle
try:
    c1 = Circle(10)
    print(c1.radius)  # _get_radius() is called
    c1.radius = 20  # _set_radius() is called
    c1.radius = -2  # _set_radius() is called
except ValueError as ex:
    print("Exception: ",ex)
