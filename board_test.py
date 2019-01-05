import unittest
from board import Board

class BoardTests(unittest.TestCase):

    def test_initial_board(self):
        b = Board()

        expected = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(b.board, expected)

    def test_player_move(self):
        b = Board()
        b.player_move(0, 0)

        expected = [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(b.board, expected)

    def test_make_move(self):
        b = Board()
        b.make_move('X', 0, 0)

        expected = [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(b.board, expected)

