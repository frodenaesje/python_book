# file: sc_08_17_temperature.py
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius   # uses the setter,
                                 # validation happens here
 
    @property
    def celsius(self):
        return self._celsius
 
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature {value} is below absolute zero")
        self._celsius = value
 
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
 
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9  # uses the celsius
                                             # setter, validation
                                             #  for free
 
    @property
    def kelvin(self):                   # no setter - read-only
        return self._celsius + 273.15
 
    def __str__(self):
        return f"{self.celsius} C | {self.fahrenheit:.1f} F | {self.kelvin:.2f} K"
 
if __name__ == "__main__":
    t = Temperature(25)
    print(t)              # 25 C | 77.0 F | 298.15 K
    t.fahrenheit = 32
    print(t.celsius)      # 0.0
    # t.kelvin = 300        # AttributeError: read-only
    # t.celsius = -300      # ValueError: below absolute zero
