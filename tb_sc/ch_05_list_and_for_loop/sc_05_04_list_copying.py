# file: sc_05_04_list_copying.py
import copy

list1 = [1, 2, 3]

# Reference assignment only (no copy)
list2 = list1
list2[0] = 10
print("After reference assignment:")
print("list1:", list1)  # [10, 2, 3]
print("list2:", list2)  # [10, 2, 3]

# Shallow copy with slicing
list1 = [1, 2, 3]
list2 = list1[:]
list2[0] = 30
print("\nAfter shallow copy with slicing:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [30, 2, 3]

# Shallow copy with list comprehension
list1 = [1, 2, 3]
list2 = [x for x in list1]
list2[0] = 40
print("\nAfter shallow copy with comprehension:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [40, 2, 3]

# Shallow copy with +
list2 = [] + list1
list2[0] = 60
print("\nAfter shallow copy with +:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [60, 2, 3]

# Shallow copy using list class copy() method
list1 = [1, 2, 3]
list2 = list1.copy()
list2[0] = 20
print("\nAfter shallow copy with copy():")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [20, 2, 3]


# Shallow copy with copy.copy()
list1 = [1, 2, 3]
list2 = copy.copy(list1)
list2[0] = 30
print("\nAfter shallow copy with copy.copy():")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [30, 2, 3]

# Deep copy
list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
list2[0] = 50
print("\nAfter deep copy:")
print("list1:", list1)  # [1, 2, 3]
print("list2:", list2)  # [50, 2, 3]
