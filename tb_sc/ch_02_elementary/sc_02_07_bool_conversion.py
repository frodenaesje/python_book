# file: sc_02_07_bool_conversion.py

# int
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True

# float
print(bool(0.0))      # False
print(bool(3.14))     # True
print(bool(-2.7))     # True

# str
print(bool(""))       # False
print(bool("text"))   # True
print(bool(" "))      # True