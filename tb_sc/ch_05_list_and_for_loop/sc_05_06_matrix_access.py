# file: sc_05_06_matrix_access.py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
value = matrix[1][2]  # Gets the value at row 1, column 2
print(value)  # Prints the value, which is 6

first_row = matrix[0]  # Gets the first row
print(first_row)  # Prints the first row, which is [1, 2, 3]

# for loop to print all values in the matrix
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# for loop to print all values in the matrix with indices
for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"matrix[{row_index}][{col_index}] = {value}")

matrix = [[1, 2], [3, 4, 5], [6]]
for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        matrix[row_index][col_index] = value * 10
print(matrix)  # [[10, 20], [30, 40, 50], [60]]

# A recursive function that traverses a list with unknown levels
def traverse(data, level=0): 
    for item in data:
        if isinstance(item, list):
            traverse(item, level + 1)
        else:
            print("  " * level + str(item))
nested = [1, [2, 3, [4, 5], 6], [7, [8, [9, 10]]]]
traverse(nested)
