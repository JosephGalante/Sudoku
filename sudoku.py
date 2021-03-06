from time import perf_counter
from math import sqrt
from copy import deepcopy

class Sudoku(object):

    def __init__(self):
        # Initialize the board
        # Use 0 for empty squares in the board
        self.board = [
            [0, 0, 0,    0, 0, 0,    0, 0, 0],
            [0, 0, 0,    0, 0, 0,    0, 0, 0],
            [0, 0, 0,    0, 0, 0,    0, 0, 0],

            [0, 0, 0,    0, 0, 0,    0, 0, 0],
            [3, 0, 0,    0, 0, 0,    1, 8, 9],
            [0, 3, 0,    0, 0, 0,    0, 0, 0],

            [0, 0, 0,    0, 0, 0,    0, 0, 0],
            [0, 0, 0,    0, 0, 0,    0, 0, 0],
            [0, 0, 0,    0, 0, 0,    0, 0, 0],
        ]
        original = deepcopy(self.board)

        if(self.is_valid()):
            self.nums = range(1, len(self.board) + 1)

            #start_time = perf_counter()
            self.solve(0, 0)
            #stop_time = perf_counter()

            if(self.board == original):
                print('This puzzle does not contain a solution')
            else:
                #print(f'It took {round(stop_time - start_time, 6)} seconds to find this solution:')
                self.print_board()

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
        for x in range(row, len(self.board)):
            for y in range(col, len(self.board)):
                if self.board[x][y] == 0:
                    return x, y

        # Finds first open 0 in the sudoku board after backtracking
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board)):
                if self.board[x][y] == 0:
                    return x, y

        # Else, return invalid coordinates
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
        
    def is_valid(self):
        
        # First check if columns are valid
        for j, col in enumerate(zip(*self.board)):
            temp = list(col)
            for i in range(temp.count(0)):
                temp.remove(0)
            if(len(temp) != len(set(temp))):
                print(f'Invalid Board: Error in column {j + 1}')
                return False


        # Then check if the rows are valid
        for j, row in enumerate(self.board):
            temp = list(row)
            for i in range(row.count(0)):
                temp.remove(0)
            if(len(temp) != len(set(temp))):                
                print(f'Invalid Board: Error in row {j + 1}')
                return False

        # Finally, check if the 3x3 grids are valid
        grid_check = (range(0, len(self.board), int(sqrt(len(self.board)))))
        root = int(sqrt(len(self.board)))

        for start_row in grid_check:
            for start_col in grid_check:
                grid = []
                for i in range(start_row, start_row + root):
                    for j in range(start_col, start_col + root):
                        grid.append(self.board[i][j])
                temp = list(grid)
                for k in range(temp.count(0)):
                    temp.remove(0)
                if(len(temp) != len(set(temp))):
                    print(f'Invalid Board: Error in local grid starting at row {start_row + 1}, column {start_col + 1}')
                    return False
                            


        # If all tests successfully pass,
        # then the board is valid, return True
        return True

    # Print the Sudoku board
    def print_board(self):
        for row in self.board:
            print(row, end = '\n')    


if __name__ == '__main__':
    sudoku = Sudoku()
    #sudoku.print_board()

    # temp = [0,0,5,6,0,2,5,7,0, 4]

    # for i in range(temp.count(0)):
    #     temp.remove(0)
    # print(temp)

    # print(len(temp) == len(set(temp)))
    
