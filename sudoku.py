import numpy as np


class Sudoku(object):

    def __init__(self):
        # Initialize the board
        # Use 0 for empty squares in the board

        self.board = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ]

        # Creates a 2D board of booleans to know which
        # Values were pre-given or if we can change those values
        # Values pre-given (non-Zero numebers) are False. 
        # Open values (0) are True
        self.given = []
        for i, row in enumerate(self.board):
            self.given.append([])
            for j, col in enumerate(row):
                if row[j] == 0:
                    self.given[i].append(True)
                else:
                    self.given[i].append(False)

        # Create array of possible values we will use to fill in board
        nums = list(range(1, len(self.board) + 1))
        print(self.is_temp_solution(1, 2, 5))


    def solve(self, row, col, num):
        print('True')


    # Returns True if the number is:
    # Not in the row, 
    # Not in the column,
    # Not in the local 3x3 grid
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


    # Returns True if number is in the local 3x3 grid, False otherwise
    def is_in_small_grid(self, row, col, num):
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if(num == self.board[i][j]):
                    return True
        return False


    # Print the Sudoku board
    def print_board(self):
        for row in self.board:
            print(row, end = '\n')    




if __name__ == '__main__':
    sudoku = Sudoku()
    