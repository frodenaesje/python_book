# File: sc_06_04_cels_to_fahr.py
# Demonstrates a code file that contains a function
# and that can be run directly or imported without running the code under if __name__ == "__main__":

# Function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# runs when the file is run directly
if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")   