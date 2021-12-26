import numpy as np
import time
from math import sqrt
import sys

class Sudoku(object):

    def __init__(self):
        # Initialize the board
        # Use 0 for empty squares in the board
        self.board = [
            [6, 0, 8, 1, 9, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 5, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 5, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 0, 6, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.nums = range(1, len(self.board) + 1)
        start_time = time.perf_counter()
        self.solve(0, 0)
        stop_time = time.perf_counter()

        print(f'It took {round(stop_time - start_time, 6)} seconds to find this solution:')

    def solve(self, i, j):
        i, j = self.next_coords(i, j)
        if(i == -1):
            return True
        
        for num in self.nums:
            if(self.is_temp_solution(i, j, num)):
                self.board[i][j] = num
                if(self.solve(i, j)):
                    return True
                self.board[i][j] = 0
        return False

    def next_coords(self, row, col):

        # Finds next 0 in the given row
        for x in range(row, 9):
            for y in range(col, 9):
                if self.board[x][y] == 0:
                    return x, y

        # Finds any open 0 in the sudoku board
        for x in range(0, 9):
            for y in range(0, 9):
                if self.board[x][y] == 0:
                    return x, y

        return -1,-1


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
    sudoku.print_board()
    