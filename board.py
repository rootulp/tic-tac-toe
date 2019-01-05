class Board:


    def __init__(self):
        self.board = self.initial_board()

    def player_move(self, row, col):
        self.make_move('X', row, col)


    def make_move(self, token, row, col):
        self.board[row][col] = token


    def initial_board(self):
        return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
