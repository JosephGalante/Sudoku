import numpy as np


class Sudoku(object):

    def __init__(self):
        self.board = [
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4],
            [3, 5, 6, 7, 1, 2, 9, 8, 4]
        ]
        self.print_board()

    def print_board(self):
        for row in self.board:
            print(row, end = '\n')    




if __name__ == '__main__':
    sudoku = Sudoku()
    