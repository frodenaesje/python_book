# File: sc_06_05_use_cels_to_fahr.py
# uses the function defined in sc_06_04_cels_to_fahr.py

import sc_06_04_cels_to_fahr as converter
# uses the function from sc_06_04_cels_to_fahr.py
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = converter.celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
