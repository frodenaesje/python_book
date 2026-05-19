# file: sc_03_01_bitwise_operations.py

a = 29  # binary: 11101
b = 15  # binary: 01111

print(f"a = {a} binary: {a:05b}")
print(f"b = {b} binary: {b:05b}")
print(f"b = {b} binary using the bin() function: {bin(b)}")

print("Bitwise operations with a = 29 and b = 15\n")

print(f"a & b  (AND): {a & b}  -> binary: {(a & b):05b}")
print(f"a | b  (OR):  {a | b}  -> binary: {(a | b):05b}")
print(f"a ^ b  (XOR): {a ^ b}  -> binary: {(a ^ b):05b}")
print(f"~a     (NOT): {~a}     -> binary: {(~a):05b} (negative number)")
print(f"a << 1 (SHIFT LEFT): {a << 1} -> binary: {(a << 1):05b}")
print(f"a >> 1 (SHIFT RIGHT): {a >> 1} -> binary: {(a >> 1):05b}")
