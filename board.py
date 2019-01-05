class Board:


    def __init__(self):
        self.board = self.initial_board()


    def make_move(self, token, row, col):
        self.board[row][col] = token


    def initial_board(self):
        return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
