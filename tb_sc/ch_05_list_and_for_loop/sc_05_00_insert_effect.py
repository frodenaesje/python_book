# file: sc_05_00_insert_effect.py
# Visual proof: id() (memory identity) of the objects does not change.
# A Python list is implemented in C as a dynamic array of references (pointers)
# to Python objects. When insert() is used, Python shifts references inside the
# list storage; the underlying objects themselves are not moved in memory.
a = {'name': 'A'}
b = {'name': 'B'}
c = {'name': 'C'}

lst = [a, c]
print([id(x) for x in lst])  # [id(a), id(c)]

lst.insert(1, b)             # Insert between a and c
print([id(x) for x in lst])  # [id(a), id(b), id(c)]  # same object ids as before

lst2 = []
lst2.append(1)
lst2.append(2)
lst2.append(3)
lst2.append(4)
print([[x, id(x)] for x in lst2])
lst2.insert(1, 5)  # Insert 5 at index 1
# Print value and id
print([[x, id(x)] for x in lst2])