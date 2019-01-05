class Board:

    PLAYER_TOKEN = 'X'
    BOT_TOKEN = 'O'
    EMPTY_TOKEN = '.'

    def __init__(self):
        self.board = self.initial_board()

    def player_move(self, row, col):
        self.make_move(self.PLAYER_TOKEN, row, col)

    def bot_make_move(self):
        row, col = self.next_empty_position()
        self.bot_move(row, col)

    def bot_move(self, row, col):
        self.make_move(self.BOT_TOKEN, row, col)

    def make_move(self, token, row, col):
        self.board[row][col] = token

    def next_empty_position(self):
        for row_i, row in enumerate(self.board):
            for col_i, token in enumerate(row):
                if token == self.EMPTY_TOKEN:
                    return row_i, col_i

        raise 'No empty positions'


    def initial_board(self):
        return [[self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN],
                [self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN],
                [self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN]]

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
