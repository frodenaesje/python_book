# file: sc_02_05_integer_interning.py
# Integer constants in the same script may refer to the same object.
# Try the corresponding assignments separately in the REPL and compare the IDs.

a = 100
b = 100
print(id(a), id(b))

a = 1000
b = 1000
print(id(a), id(b))
