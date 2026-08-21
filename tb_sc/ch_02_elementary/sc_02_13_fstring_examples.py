# file: sc_02_13-fstring_examples.py
# Demonstrates different ways to use f-strings in Python

import math

# --- Simple use ---
name = "John"
print(f"Hello {name}!")

# --- Expressions in placeholder ---
radius = 2
print(f"The area of a circle with radius {radius} is {math.pi * radius**2:.2f}")
print(f"The area of a circle with radius {radius} is {math.pi * math.pow(radius, 2):.2f}")

# --- Decimal precision ---
area = math.pi * radius**2
print(f"The area is {area:.2f}")    # two decimal places
print(f"The area is {area:.4f}")    # four decimal places
print(f"The area is {area:.2e}")    # scientific notation

# --- Comma separators ---
large_number = 1234567890.12345
print(f"{large_number:,.2f}")              # 1,234,567,890.12

# --- Leading zeros ---
number = 9
print(f"Leading zero demo, width 3: {number:03}")   # 009

# --- Percentage ---
discount = 0.5
print(f"Discount {discount:.0%}")      # 50%

# --- Field width and alignment ---
print(f"\nRight-aligned (default):")
print(f"{'Day':15}{'Temperature':10}")
print(f"{'Monday':15}{20.5:10}")
print(f"{'Tuesday':15}{18.2:10}")
print(f"{'Wednesday':15}{22.8:10}")

print(f"\nLeft-aligned:")
print(f"{'Day':15}{'Temperature':10}")
print(f"{'Monday':15}{20.5:<10}")
print(f"{'Tuesday':15}{18.2:<10}")
print(f"{'Wednesday':15}{22.8:<10}")

print(f"\nCentered:")
print(f"{'Day':^15}{'Temperature':^10}")
print(f"{'Monday':^15}{20.5:^10}")
print(f"{'Tuesday':^15}{18.2:^10}")
print(f"{'Wednesday':^15}{22.8:^10}")

# --- Variables in the format specifier ---
width     = 10
precision = 4
value     = 3.14159265
print(f"\n{value:{width}.{precision}f}")

# --- Concatenating f-strings ---
some_data = 555
part1 = f"First part with some data {some_data}"
part2 = f" followed by this"
print(part1 + part2)
