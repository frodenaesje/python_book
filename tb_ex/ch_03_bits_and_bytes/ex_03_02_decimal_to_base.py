# file: ex_03_02_decimal_to_base.py

original = int(input("Enter a positive integer: "))

# --- Part 1: decimal to binary ---
number = original
binary_str = ""
while number > 0:
    binary_str = str(number % 2) + binary_str
    number //= 2

print(f"Binary (manual):   {binary_str}")
print(f"Binary (built-in): {bin(original)}")

print()

# --- Part 2: decimal to hexadecimal ---
hex_digits = "0123456789ABCDEF"
number = original
hex_str = ""
while number > 0:
    hex_str = hex_digits[number % 16] + hex_str
    number //= 16

print(f"Hexadecimal (manual):   {hex_str}")
print(f"Hexadecimal (built-in): {hex(original)}")
