// Sudoku Solver
// for leetcode problems
// 2015.04.16 by zhanglin

// Problem Link:
// https://leetcode.com/problems/sudoku-solver/

// Problem:
// Write a program to solve a Sudoku puzzle by filling the empty cells.

// Empty cells are indicated by the character '.'.

// You may assume that there will be only one unique solution.

// Pictrue refer to: https://leetcode.com/problems/sudoku-solver/

// |5|3| | |7| | | | |
// |6| | |1|9|5| | | |
// | |9|8| | | | |6| |
// |8| | | |6| | | |3|
// |4| | |8| |3| | |1|
// |7| | | |2| | | |6|
// | |6| | | | |2|8| |
// | | | |4|1|9| | |5|
// | | | | |8| | |7|9|

// A sudoku puzzle...

// |5|3|4|6|7|8|9|1|2|
// |6|7|2|1|9|5|3|4|8|
// |1|9|8|3|4|2|5|6|7|
// |8|5|9|7|6|1|4|2|3|
// |4|2|6|8|5|3|7|9|1|
// |7|1|3|9|2|4|8|5|6|
// |9|6|1|5|3|7|2|8|4|
// |2|8|7|4|1|9|6|3|5|
// |3|4|5|2|8|6|1|7|9|

public class Solution {
    public void solveSudoku(char[][] board) {
        doSolveSudoku(board);
    }

    public boolean doSolveSudoku(char[][] board) {
        for(int row = 0; row < 9; row++) {
            for(int column = 0; column < 9; column++) {
                if(board[row][column] == '.') {
                    for(char c = '1'; c <= '9'; c++) {
                        board[row][column] = c;

                        if(isValid(board, row, column) && doSolveSudoku(board)) {
                            return true;
                        }

                        else {
                            board[row][column] = '.';
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    public boolean isValid(char[][] board, int this_row, int this_column) {
        char this_num = board[this_row][this_column];
        board[this_row][this_column] = '.';

        for(int row = 0; row < 9; row++) {
            if(board[row][this_column] == this_num) {
                board[this_row][this_column] = this_num;
                return false;
            }
        }

        for(int column = 0; column < 9; column++) {
            if(board[this_row][column] == this_num) {
                board[this_row][this_column] = this_num;
                return false;
            }
        }

        int base_row    = this_row    / 3 * 3;
        int base_column = this_column / 3 * 3;

        for(int sub_row = 0; sub_row < 3; sub_row++) {
            for(int sub_column = 0; sub_column < 3; sub_column++) {
                int real_row    = base_row + sub_row;
                int real_column = base_column + sub_column;

                if(board[real_row][real_column] == this_num) {
                    return false;
                }
            }
        }

        board[this_row][this_column] = this_num;
        return true;
    }
}


