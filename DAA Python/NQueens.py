# Function to print the solution
def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# A utility function to check if a queen can
# be placed on board[row][col]. We only check the left side
# for attacking queens as the queens are placed from left to right.
def isSafe(board, row, col, N):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Recursive utility to solve the N Queen problem
def solveNQUtil(board, col, N):

    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing a queen in all rows one by one for this column
    for i in range(N):

        if isSafe(board, i, col, N):
            # Place this queen on board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solveNQUtil(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then backtrack and remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False


# Function to solve the N-Queens problem
def solveNQ(N):
    # Initialize the board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    # If no solution exists, print a message
    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
        return False

    # Print the solution
    printSolution(board, N)
    return True


# Driver code with user input
if __name__ == '__main__':
    # Ask user for input for the size of the board
    N = int(input("Enter the value of N for an N x N chessboard: "))
    solveNQ(N)
