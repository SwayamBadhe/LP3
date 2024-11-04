def is_safe(board, row, col, n):
    # Check the column and both diagonals
    for i in range(row):
        if board[i][col] == 'Q' or \
           (col - row + i >= 0 and board[i][col - row + i] == 'Q') or \
           (col + row - i < n and board[i][col + row - i] == 'Q'):
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        return True  # All queens are placed successfully

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = '.'  # Backtrack if not valid
    return False

def n_queens(n):
    # Initialize the board with the first queen placed in the first row
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[0][0] = 'Q'  # First queen in the top-left corner

    # Solve the rest of the board
    if solve_nqueens(board, 1, n):  # Start from the second row
        for row in board:
            print(" ".join(row))
    else:
        print("No solution exists.")

# Driver code
n = int(input("Enter the value of n: "))
n_queens(n)
