# file: sc_02_05_integer_interning.py
# Demonstrerer Pythons integer interning

# Python caches small integers (typically between -5 and 256) to save memory
# and improve performance. This means that when you create an integer within this range,
# Python will reuse the existing object instead of creating a new one.

a = 100
b = 100
print(id(a), id(b))  # Same object in memory
a = 1000
b = 1000
print(id(a), id(b))  # Different objects in memory
a = 100000
j = "text"
b = 100000
print(id(a), id(b))  # Different objects in memory
# This is because Python does not cache larger integers, so each time you create
# a new integer outside of the cached range, Python creates a new object in memory.
# This behavior is an implementation detail of CPython, the standard Python interpreter.
# Other implementations of Python may have different caching strategies.