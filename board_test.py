import unittest
from board import Board

class BoardTests(unittest.TestCase):

    def test_initial_board(self):
        b = Board()

        expected = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.assertEqual(b.board, expected)

