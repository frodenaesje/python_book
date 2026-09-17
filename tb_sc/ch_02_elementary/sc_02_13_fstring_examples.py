# file: sc_02_13_fstring_examples.py
# Demonstrates different ways to use f-strings in Python

import math

# --- Simple use ---
name = input("What's your name?")
print(f"Hello {name}!")

name = "John"
greeting = f"Hello {name}"
print(greeting + ", welcome!")

# --- Expressions in placeholder ---
radius = 2
print(f"The area of a circle with radius {radius} is {math.pi * radius**2:.2f}")
print(f"The area of a circle with radius {radius} is {math.pi * math.pow(radius, 2):.2f}")

# --- Decimal precision ---
area = math.pi * radius**2
print(f"Area is {area:.2f}")    # two decimal places
print(f"Area is {area:.4f}")    # four decimal places
print(f"Area is {area:.2e}")    # scientific notation

# --- Comma separators ---
number = 1234567890.12345
print(f"{number:,.2f}")              # 1,234,567,890.12

# --- Leading zeros ---
number = 9
print(f"{number:03}")   # 009

# --- Percentage ---
discount = 0.5
print(f"Discount {discount:.0%}")      # 50%

# --- Field width and alignment ---
print(f"{'Day':15}{'Temperature':10}")
print(f"{'Monday':15}{20.5:10}")
print(f"{'Tuesday':15}{18.2:10}")
print(f"{'Wednesday':15}{22.8:10}")

print(f"{'Day':^15}{'Temperature':^10}")
print(f"{'Monday':^15}{20.5:^10}")
print(f"{'Tuesday':^15}{18.2:^10}")
print(f"{'Wednesday':^15}{22.8:^10}")

# --- Variables in the format specifier ---
width     = 10
precision = 4
value     = 3.14159265
print(f"{value:{width}.{precision}f}")

# --- Concatenating f-strings ---
some_data = 555
part1 = f"First part and some data {some_data}"
part2 = f" followed by this"
print(part1 + part2)
