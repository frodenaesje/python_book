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
    for value in row:
        print(value, end=' ')  # Prints values in the same row
    print()  # Go to next line after each row

# for loop to print all values in the matrix with indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}", end=' ')
    print()  # Go to next line after each row

# change a value in the matrix
matrix[0][0] = 10  # Changes the value at row 0, column 0
print("After change:", matrix)  # Prints the matrix after the change

# copy a two-dimensional list in various ways
matrix_copy1 = matrix.copy()  # Copies the reference to the outer list
matrix_copy2 = [row.copy() for row in matrix]  # Copies each row individually
print("Copied matrix (reference):", matrix_copy1)
print("Copied matrix (individual rows):", matrix_copy2)
