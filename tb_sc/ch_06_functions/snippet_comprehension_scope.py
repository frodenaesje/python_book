# file: snippet_comprehension_scope.py
# A comprehension creates its own scope.
# Its loop variable does not leak out; accessing i here raises NameError.

a_list = [i for i in range(5)]
print(i)  # NameError: i is not defined
