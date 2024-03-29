import unittest
from board import Board


class BoardTests(unittest.TestCase):

    def setUp(self):
        self.b = Board()
        return super().setUp()

    def test_initial_board(self):
        expected = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(self.b.board, expected)

    def test_player_move(self):
        self.b.player_move(0, 0)

        expected = [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(self.b.board, expected)

    def test_bot_move(self):
        self.b.bot_move(1, 1)

        expected = [['.', '.', '.'], ['.', 'O', '.'], ['.', '.', '.']]
        self.assertEqual(self.b.board, expected)

    def test_make_move(self):
        self.b.make_move('X', 0, 0)

        expected = [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(self.b.board, expected)

    def test_bot_make_move(self):
        self.b.bot_make_move()

        expected = [['O', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(self.b.board, expected)
