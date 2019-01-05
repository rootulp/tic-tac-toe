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
            for col_i, _token in enumerate(row):
                if self.is_empty_position(row_i, col_i):
                    return row_i, col_i

        raise 'No empty positions'

    def initial_board(self):
        return [[self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN],
                [self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN],
                [self.EMPTY_TOKEN, self.EMPTY_TOKEN, self.EMPTY_TOKEN]]

    def score(self):
        if not self.is_game_over():
            return 0

    def is_game_over(self):
        return self.any_three_in_row() or self.any_three_in_col() or self.any_three_in_diag()

    def any_three_in_row(self):
        return self.is_three_in_row(0) or self.is_three_in_row(1) or self.is_three_in_row(2)

    def is_three_in_row(self, row_i):
        not_empty = not self.is_empty_position(row_i, 0)
        three_in_row = self.board[row_i][0] == self.board[row_i][1] == self.board[row_i][2]
        return not_empty and three_in_row

    def any_three_in_col(self):
        return self.is_three_in_col(0) or self.is_three_in_col(1) or self.is_three_in_col(2)

    def is_three_in_col(self, col_i):
        not_empty = not self.is_empty_position(0, col_i)
        three_in_col = self.board[0][col_i] == self.board[1][col_i] == self.board[2][col_i]
        return not_empty and three_in_col

    def any_three_in_diag(self):
        # There are only two diagonals in the board
        not_empty_diag_1 = not self.is_empty_position(0, 0)
        three_in_diag_1 = self.board[0][0] == self.board[1][1] == self.board[2][2]
        not_empty_diag_2 = not self.is_empty_position(2, 0)
        three_in_diag_2 = self.board[2][0] == self.board[1][1] == self.board[0][2]
        return (not_empty_diag_1 and three_in_diag_1) or (not_empty_diag_2 and three_in_diag_2)

    def is_empty_position(self, row_i, col_i):
        return self.board[row_i][col_i] == self.EMPTY_TOKEN

    def __str__(self):
        output = ['Board:']

        for row in self.board:
            output.append(''.join(row))

        return '\n'.join(output)

def main():
    b = Board()

    while not b.is_game_over():
        print(b, end='\n====================================\n')
        row_i, col_i = list(map(int, input('Player move: ').strip().split(' ')))
        b.player_move(row_i, col_i)

        if b.is_game_over():
            print('Player wins!')
            break
        else:
            b.bot_make_move()

if __name__ == '__main__':
    main()
