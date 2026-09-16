# file: sc_07_08_set_demo.py
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "orange", "grape"}

# union - everything from both
print(fruits1 | fruits2)
# {"apple", "banana", "orange", "cherry", "grape"}

# intersection - common elements
print(fruits1 & fruits2)
# {"banana"}

# difference - in fruits1 but not fruits2
print(fruits1 - fruits2)
# {"apple", "cherry"}

# symmetric difference - not common
print(fruits1 ^ fruits2)
# {"apple", "cherry", "orange", "grape"}

# subset and superset
small = {"banana"}
print(small <= fruits1)   # True - small is a subset of fruits1
print(fruits1 >= small)   # True - fruits1 is a superset of small

# membership check
print("apple" in fruits1)   # True
print("orange" in fruits1)  # False
