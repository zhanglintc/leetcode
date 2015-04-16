# Sudoku Solver
# for leetcode problems
# 2015.03.20 by zhanglin

# Problem:
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.

# Pictrue refer to: https://leetcode.com/problems/sudoku-solver/

# |5|3| | |7| | | | |
# |6| | |1|9|5| | | |
# | |9|8| | | | |6| |
# |8| | | |6| | | |3|
# |4| | |8| |3| | |1|
# |7| | | |2| | | |6|
# | |6| | | | |2|8| |
# | | | |4|1|9| | |5|
# | | | | |8| | |7|9|

# A sudoku puzzle...

# |5|3|4|6|7|8|9|1|2|
# |6|7|2|1|9|5|3|4|8|
# |1|9|8|3|4|2|5|6|7|
# |8|5|9|7|6|1|4|2|3|
# |4|2|6|8|5|3|7|9|1|
# |7|1|3|9|2|4|8|5|6|
# |9|6|1|5|3|7|2|8|4|
# |2|8|7|4|1|9|6|3|5|
# |3|4|5|2|8|6|1|7|9|

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # solveSudoku cannot return anything, so we call another function
        self.doSolveSudoku(board)

    def doSolveSudoku(self, board):
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    for i in range(1, 9 + 1): # from 1 to 9
                        board[row][column] = str(i)

                        # if this position is OK && resest of board is OK, return True
                        if self.isValid(board, row, column) and self.doSolveSudoku(board):
                            return True

                        # else restore this position
                        else:
                            board[row][column] = '.'

                    # no number fit this position, return False
                    return False

        # every position is OK, return True
        return True

    def isValid(self, board, this_row, this_column):
        # store this_num and replace it with '.'
        this_num = board[this_row][this_column]
        board[this_row][this_column] = '.'

        # check row
        for row in range(9):
            if board[row][this_column] == this_num:
                board[this_row][this_column] = this_num
                return False

        # check column
        for column in range(9):
            if board[this_row][column] == this_num:
                board[this_row][this_column] = this_num
                return False

        # check sub-box
        base_row    = this_row    / 3 * 3
        base_column = this_column / 3 * 3

        for sub_row in range(3):
            for sub_column in range(3):
                real_row    = base_row + sub_row
                real_column = base_column + sub_column

                if board[real_row][real_column] == this_num:
                    return False

        # all well, restore this_num and return True
        board[this_row][this_column] = this_num
        return True


