import numpy as np
import time
from math import sqrt
import sys

class Sudoku(object):

    def __init__(self):

        # Initialize the board
        # Use 0 for empty squares in the board
        self.board = [
            [6, 2, 8, 1, 9, 5, 7, 4, 3],
            [4, 0, 0, 0, 0, 8, 0, 5, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 0, 3, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 1, 0, 6, 0, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 7, 6, 0, 0],
            [0, 6, 5, 0, 2, 4, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 8, 7]
        ]
        self.nums = range(1, len(self.board) + 1)

        start_time = time.perf_counter()
        self.solve()
        stop_time = time.perf_counter()

        print(f'It took {stop_time - start_time} seconds to find this solution:')
        

    def solve(self):

        for i, row in enumerate(self.board):
            for j, col in enumerate(row): 
                if (self.board[i][j] == 0):
                    for num in self.nums:
                        if (self.is_temp_solution(i, j, num) is True):
                            self.board[i][j] = num
                            self.solve()
                            self.board[i][j] = 0
                    return
        [print(row) for row in self.board]


    # Returns True if the number is:
    # Not in the row AND
    # Not in the column AND
    # Not in the local 3x3 self.board
    def is_temp_solution(self, row, col, num):
        if(not self.is_in_row(row, num) and not self.is_in_col(col, num) and not self.is_in_small_grid(row, col, num)):
            return True
        else:
            return False

    # Returns whether the number is in the board's row
    def is_in_row(self, row, num):
        return (num in self.board[row])

    # Returns whether number is in the board's column
    def is_in_col(self, col, num):
        col_nums = [row[col] for row in self.board]
        return (num in col_nums)

    # Returns True if number is in the local 3x3 self.board, False otherwise
    def is_in_small_grid(self, row, col, num):
        root = int(sqrt(len(self.board)))
        start_row = (row // root) * root
        start_col = (col // root) * root
        for i in range(start_row, start_row + root):
            for j in range(start_col, start_col + root):
                if(num == self.board[i][j]):
                    return True
        return False


    # Print the Sudoku board
    def print_board(self):
        for row in self.board:
            print(row, end = '\n')    


if __name__ == '__main__':
    sudoku = Sudoku()
    
    