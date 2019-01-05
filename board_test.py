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

    def test_when_game_is_not_over(self):
        self.assertFalse(self.b.is_game_over())

    def test_when_game_is_over(self):
        self.b.player_move(0, 0)
        self.b.player_move(1, 1)
        self.b.player_move(2, 2)

        self.assertTrue(self.b.is_game_over())

    def test_score_is_zero_when_game_is_not_over(self):
        expected = 0
        self.assertEqual(self.b.score(), expected)

    def test_score_is_positive_one_when_player_wins(self):
        self.b.player_move(0, 0)
        self.b.player_move(1, 1)
        self.b.player_move(2, 2)

        expected = 1
        self.assertEqual(self.b.score(), expected)

    def test_score_is_negative_one_when_bot_wins(self):
        self.b.bot_move(0, 0)
        self.b.bot_move(1, 1)
        self.b.bot_move(2, 2)

        expected = -1
        self.assertEqual(self.b.score(), expected)
