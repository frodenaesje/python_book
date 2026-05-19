# file: sc_07_08_set_demo.py
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "orange", "grape"}

# Union - alt fra begge
print(fruits1 | fruits2)
# {"apple", "banana", "orange", "cherry", "grape"}

# Snitt - felles
print(fruits1 & fruits2)
# {"banana"}

# Differanse - i fruits1 men ikke fruits2
print(fruits1 - fruits2)
# {"apple", "cherry"}

# Symmetrisk differanse - ikke felles
print(fruits1 ^ fruits2)
# {"apple", "cherry", "orange", "grape"}

# Delmengde og supermengde
small = {"banana"}
print(small <= fruits1)   # True - small er delmengde av fruits1
print(fruits1 >= small)   # True - fruits1 er supermengde av small

# Medlemskapssjekk
print("apple" in fruits1)   # True
print("orange" in fruits1)  # False
