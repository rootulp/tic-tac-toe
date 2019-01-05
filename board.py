class Board:

    def __init__(self):
        self.board = self.initial_board()

    def player_move(self, row, col):
        self.make_move('X', row, col)

    def bot_make_move(self):
        row, col = self.next_open_position()
        self.bot_move(row, col)

    def bot_move(self, row, col):
        self.make_move('O', row, col)

    def make_move(self, token, row, col):
        self.board[row][col] = token

    def next_open_position(self):
        for row_i, row in enumerate(self.board):
            for col_i, token in enumerate(row):
                if token == '.':
                    return row_i, col_i

        raise 'No open positions'


    def initial_board(self):
        return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def __str__(self):
        output = ['Board:']

        for row in self.board:
            output.append(''.join(row))

        return '\n'.join(output)

def main():
    b = Board()
    print(b)

if __name__ == "__main__":
    main()
