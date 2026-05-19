# file: sc_08_01_Car.py
# This code defines a simple class `Car` with methods to "drive" :-)
# and show information about the car.
class Car:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color
    
    def drive(self):
        print(f"{self._brand} car is driving!")
    
    def show_info(self):
        print(f"Car: {self._brand}, Color: {self._color}")

# Create two car objects
my_car = Car("Toyota", "Blue")
another_car = Car("Volvo", "Red")

# Use the methods
my_car.drive()        # Output: Toyota car is driving!
my_car.show_info()    # Output: Car: Toyota, Color: Blue
another_car.show_info()  # Output: Car: Volvo, Color: Red