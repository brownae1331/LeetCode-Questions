"""
Question:
        You are given a 9 x 9 Sudoku board. A Sudoku board is valid if the following rules are followed:
        1. Each row must contain the digits 1-9 without duplicates.
        2. Each column must contain the digits 1-9 without duplicates.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

        Return true if the Sudoku board is valid, otherwise return false

        Note: A board does not need to be full or be solvable to be valid.
"""

from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:
    """
    It uses three dictionaries of sets to track which numbers have been seen in each row, column, and sub-box.
    As it iterates through each cell, it skips empty cells (".") and return False immediately if a duplicate is found.

    Time complexity: O(n^2) - There are two nested for loops that loop over the size of the board.
    Space complexity: O(n) - There are 3 seperate dictionaries that have n elements.
    """
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True

if __name__ == "__main__":
    output = isValidSudoku(board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])
    print(output)