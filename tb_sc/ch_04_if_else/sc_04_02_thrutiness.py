# file: sc_04_02_thrutiness.py
# Demonstrates truthiness and falsiness in Python

print(bool(0))       # False
print(bool(1))       # True
print(bool(-5))      # True
print(bool(None))    # False
print(bool(""))      # False
print(bool("Hi"))   # True
print(bool(" "))     # True
print(bool([]))      # False
print(bool([1, 2]))  # True

no_value = None
if not no_value:
    print("No value set")

name = "Ada"

if bool(name):
    print("Name provided")

if name:
    print("Name provided")
