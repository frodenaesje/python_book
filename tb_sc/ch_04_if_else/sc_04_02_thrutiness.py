# file: sc_04_02_thrutiness.py
# Demonstrates truthiness and falsiness in Python

print(bool(0))       # False
print(bool(1))       # True
print(bool(None))    # False
print(bool(""))      # False
print(bool("Hei"))   # True
print(bool([]))      # False
print(bool([1, 2]))  # True

print('if 0:', 'True' if 0 else 'False') # False
print('if 1:', 'True' if 1 else 'False') # True
print('if None:', 'True' if None else 'False') # False
print('if "":', 'True' if "" else 'False') # False
print('if "Hello":', 'True' if "Hello" else 'False') # True
print('if []:', 'True' if [] else 'False') # False
print('if [1, 2]:', 'True' if [1, 2] else 'False') # True