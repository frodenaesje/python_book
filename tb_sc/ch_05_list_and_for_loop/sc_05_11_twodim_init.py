#  file: sc_05_11_twodim_init.py
# Initialization of a two-dimensional list (matrix) with loops and with comprehension

NUM_ROWS = 3
NUM_COLS = 3
matrix = []
for i in range(NUM_ROWS):
    row = [] # start with an empty row for each row level
    for j in range(NUM_COLS):
        row.append(i * NUM_COLS + j + 1) # Fill with numbers from 1 to 9
    matrix.append(row)
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# same with comprehension
matrix = [[i * NUM_COLS + j + 1 for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = 5
grid = []
for k in range(N):
    grid.append([])
    for _ in range(N):
        grid[k].append(False)
print(grid)

grid = [[False for _ in range(N)] for k in range(N)]
print(grid)
