# Created by Manan Shah
# Algorithm for solving sudoku using the backtracking algorithm.
# In this program, a 0 in the board signifies an empty cell.

import time
# function to spot the next empty cell in the board. It traverses a row and returns the row and col of the cell
def findEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def printBoard(board):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - -")
        for j in range(col):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]), " ", end="")


def validateEntry(num, board, pos):
    # checking rows
    for col in range(9):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # checking cols
    for row in range(9):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # checking boxes:
    # compute the box of the current entry
    Xbox = pos[1] // 3
    Ybox = pos[0] // 3
    for i in range(Ybox * 3, Ybox * 3 + 3):
        for j in range(Xbox * 3, Xbox * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def backTrack(board):
    # Solving the sudoku problem using backtracking and recursion
    find = findEmptyCell(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validateEntry(i, board, (row, col)):
            board[row][col] = i

            if backTrack(board):
                return True

            board[row][col] = 0

    return False


sudoku_board = [[9, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 8, 0, 0, 0],
                [1, 0, 5, 7, 9, 0, 4, 6, 0],
                [0, 5, 0, 0, 4, 0, 1, 2, 6],
                [4, 0, 0, 0, 0, 0, 0, 0, 7],
                [6, 3, 1, 0, 2, 0, 0, 4, 0],
                [0, 2, 4, 0, 6, 5, 8, 0, 1],
                [0, 0, 0, 1, 0, 0, 9, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 4]]

printBoard(sudoku_board)
start = time.time()
backTrack(sudoku_board)
time_taken = time.time() - start
print("__________________________________________________________")
printBoard(sudoku_board)
print("\n",time_taken," s")
