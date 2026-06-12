# file: ex_03_04_bitwise_explorer.py

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

print()
print(f"a        = {a}  ({bin(a)})")
print(f"b        = {b}  ({bin(b)})")
print()
print(f"a & b    = {a & b}  ({bin(a & b)})   AND:   only bits set in BOTH")
print(f"a | b    = {a | b}  ({bin(a | b)})   OR:    bits set in EITHER")
print(f"a ^ b    = {a ^ b}  ({bin(a ^ b)})   XOR:   bits set in ONE but not BOTH")
print(f"~a       = {~a} ({bin(~a)})  NOT:   flips all bits (two's complement)")
print(f"a << 1   = {a << 1}  ({bin(a << 1)})  LEFT:  shift bits left (multiply by 2)")
print(f"a >> 1   = {a >> 1}  ({bin(a >> 1)})    RIGHT: shift bits right (divide by 2)")
