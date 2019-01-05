import numpy as np
import random
from time import sleep

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

    def is_game_over(self):
        return self.evaluate_board() != -1

    # Check for empty places on board
    def possibilities(self):
        l = []

        for i in range(len(self.board)):
            for j in range(len(self.board)):

                if self.is_empty_position(i, j):
                    l.append((i, j))

        return(l)

    # Select a random place for the player
    def random_place(self, player):
        selection = self.possibilities()
        row, col = random.choice(selection)
        self.board[row][col] = player
        return(self.board)

    # Evaluates whether there is a winner or a tie
    def evaluate_board(self):
        winner = 0

        for player in (self.PLAYER_TOKEN, self.BOT_TOKEN):
            if (self.row_win(player) or
                self.col_win(player) or
                self.diag_win(player)):

                winner = player

        if self.is_board_full() and winner == 0:
            winner = -1

        return winner

    def is_board_full(self):
        for row_i, row in enumerate(self.board):
            for col_i, _token in enumerate(row):
                if self.is_empty_position(row_i, col_i):
                    return False
        return True


    # Checks whether the player has three of their marks in a horizontal row
    def row_win(self, player):
        for x in range(len(self.board)):
            win = True

            for y in range(len(self.board)):
                if self.board[x][y] != player:
                    win = False
                    continue

            if win == True:
                return(win)
        return(win)

    # Checks whether the player has three of their marks in a vertical row
    def col_win(self, player):
        for x in range(len(self.board)):
            win = True

            for y in range(len(self.board)):
                if self.board[y][x] != player:
                    win = False
                    continue

            if win == True:
                return(win)
        return(win)

    # Checks whether the player has three of their marks in a diagonal row
    def diag_win(self, player):
        win = True

        for x in range(len(self.board)):
            if self.board[x][x] != player:
                win = False
        return(win)

    def is_empty_position(self, row_i, col_i):
        return self.board[row_i][col_i] == self.EMPTY_TOKEN

    def __str__(self):
        output = ['Board:']

        for row in self.board:
            output.append(''.join(row))

        return '\n'.join(output)

# Main function to start the game
def play_game():
    board = Board()
    winner = 0
    move_count = 0

    print(board)
    while winner == 0:
        for player in [board.PLAYER_TOKEN, board.BOT_TOKEN]:
            board.random_place(player)
            print("Board after " + str(move_count) + " move")
            print(board)
            sleep(2)
            move_count += 1
            winner = board.evaluate_board()
            if winner != 0:
                break

    return(winner)


if __name__ == '__main__':
    print("Winner is: " + str(play_game()))
