# file: sc_03_00_number_vs_char.py

a = 1
b = '1'

print("Value of a:", a)   # Value of a: 1
print("Value of b:", b)   # Value of b: 1

print("Type a:", type(a)) # <class 'int'>
print("Type b:", type(b)) # <class 'str'>

print("a + a =", a + a)  # 2  – integer addition
print("b + b =", b + b)  # 11 – string concatenation

print("a + b =", a + b)  # illegal, will print a TypeError msg