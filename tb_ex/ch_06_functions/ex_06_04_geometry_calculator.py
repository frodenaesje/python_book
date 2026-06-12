# file: ex_06_04_geometry_calculator.py
import math

def rectangle(width: float, height: float) -> tuple:
    """Return (area, perimeter) for a rectangle."""
    return width * height, 2 * (width + height)

def circle(radius: float) -> tuple:
    """Return (area, perimeter) for a circle."""
    return math.pi * radius**2, 2 * math.pi * radius

def right_triangle(a: float, b: float) -> tuple:
    """Return (area, perimeter) for a right triangle with legs a and b."""
    hypotenuse = math.sqrt(a**2 + b**2)
    return 0.5 * a * b, a + b + hypotenuse


if __name__ == "__main__":
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Right triangle")
    choice = input("Your choice: ")

    match choice:
        case "1":
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            area, perimeter = rectangle(w, h)
            label = f"Rectangle {w} x {h}"
        case "2":
            r = float(input("Enter radius: "))
            area, perimeter = circle(r)
            label = f"Circle with radius {r}"
        case "3":
            a = float(input("Enter leg a: "))
            b = float(input("Enter leg b: "))
            area, perimeter = right_triangle(a, b)
            label = f"Right triangle with legs {a} and {b}"
        case _:
            print("Invalid choice.")
            exit()

    print(f"{label}:")
    print(f"  Area:      {area:.2f}")
    print(f"  Perimeter: {perimeter:.2f}")
