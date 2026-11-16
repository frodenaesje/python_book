# file: sc_03_07_rgb_code.py

red = int(input("Red (0-255): "))
green = int(input("Green (0-255): "))
blue = int(input("Blue (0-255): "))

colour_code = f"#{red:02X}{green:02X}{blue:02X}"

print(f"Colour code: {colour_code}")
