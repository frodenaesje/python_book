# sc_05_10_comprehension_demo.py

# Traditional for loop
squares = []
for x in range(10):
    squares.append(x * x)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent comprehension
squares = [x * x for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With filter: [expression for item in collection if condition]
odd_squares = [x*x for x in range(10) if x % 2 != 0]
print(odd_squares) # [1, 9, 25, 49, 81]

# Nested loops in one comprehension
# Traditional:
result = []
for x in range(3):
    for y in range(2):
        result.append(x * y)
print(result) # [0, 0, 0, 1, 0, 2] # all goes into the same list

# Comprehension:
result = [x * y for x in range(3) for y in range(2)]
print(result) # [0, 0, 0, 1, 0, 2] # all goes into the same list

# Multidimensional comprehensions
# Traditional
result = []
for x in range(3):          # outer [] - outer loop, builds result
    row = []                # inner [] - a fresh list per x
    for y in range(2):      # inner for - fills the row
        row.append(x * y)   # the expression - what we append
    result.append(row)      # inner [] closed - add row to result
print(result) # [[0, 0], [0, 1], [0, 2]]

# Comprehension
result = [[x * y for y in range(2)] for x in range(3)]
print(result) # [[0, 0], [0, 1], [0, 2]]
