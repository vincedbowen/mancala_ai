from unittest import TestCase
from board.mancala_board import Board


class TestBoard(TestCase):
    def test_play(self):
        board = Board()
        board.play(4)
        board.render_board()
        self.assertEqual(board.player_one_side['mancala'], 1)
        self.assertEqual(board.current_player, 1)
