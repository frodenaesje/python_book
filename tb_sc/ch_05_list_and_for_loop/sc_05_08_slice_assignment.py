# file: sc_05_08_slice_assignment.py

list1 = [0, 1, 2, 3, 4, 5]
list1[1:4] = [10, 11, 12] # replaces elements
print(list1) # [0, 10, 11, 12, 5]

list1[2:4] = [] # removes elements
print(list1) # [0, 10, 5]

list1[1:1] = [99, 100]  # Inserts two elements before index 1
print(list1) # [0, 99, 100, 10, 5]
