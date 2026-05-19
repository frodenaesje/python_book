# file: sc_18_04_eight_queens_implementations.py

def eight_queens_iterative(size=8):
    
    board = [-1] * size # Initialize board with -1 indicating no queen placed
    
    def is_valid(row, col):
        for i in range(row):
            if (board[i] == col  # Check column
                or board[i] == col - row + i  # Check upleft diagonal
                or board[i] == col + row - i):  # Upright diagonal
                return False
        return True
    
    def find_position(row):
        start = board[row] + 1 #
        for col in range(start, size):
            if is_valid(row, col):
                return col # Found valid position for queen in this row
        return size # No valid position found, signal to backtrack
    
    # Iterative backtracking approach.
    # Code start here, use inner functions for clarity.
    row = 0 
    while 0 <= row < size: # Loop until we either find a solution or exhaust all possibilities
        col = find_position(row)
        if col == size: # No valid position found, backtrack
            board[row] = -1
            row -= 1
        else:
            board[row] = col # Place queen
            row += 1
    
    return board if row == size else None


def eight_queens_recursive(size=8):
   
    # More Pythonic recursive backtracking approach.
    
    def is_valid(row, col, board):
        for i in range(row):
            if (board[i] == col  # Check column
                or board[i] == col - row + i  # Check upleft diagonal
                or board[i] == col + row - i):  # Upright diagonal
                return False
        return True
    
    def backtrack(row, board):
        if row == size:
            return board  # All queens placed successfully
        
        for col in range(size):
            if is_valid(row, col, board):
                board[row] = col  # Place queen
                result = backtrack(row + 1, board)
                if result is not None:
                    return result
                # Implicit backtracking: just try next col
        
        return None  # No solution found in this branch
    
    return backtrack(0, [-1] * size)


def print_board(board, size=8):
    """Print the chessboard with queens."""
    if board is None:
        print("No solution found")
        return
    
    for row in range(size):
        for col in range(size):
            print("Q " if board[row] == col else "* ", end="")
        print()


# Test both implementations
if __name__ == "__main__":
    print("Iterative backtracking solution:")
    board1 = eight_queens_iterative()
    print_board(board1)
    
    print("\nRecursive backtracking solution:")
    board2 = eight_queens_recursive()
    print_board(board2)