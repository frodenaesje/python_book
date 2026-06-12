# file: ex_06_04_geometry_calculator_start.py
import math

# TODO: Write rectangle(width: float, height: float) -> tuple
#       Returns (area, perimeter)

# TODO: Write circle(radius: float) -> tuple
#       Returns (area, perimeter)
#       Use math.pi

# TODO: Write right_triangle(a: float, b: float) -> tuple
#       Returns (area, perimeter)
#       Hint: hypotenuse = math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Right triangle")
    choice = input("Your choice: ")

    # TODO: Use match-case (or if-elif) to read the right dimensions
    #       and call the correct function
    #       Unpack the returned tuple: area, perimeter = function(...)
    #       Print area and perimeter formatted to 2 decimal places
