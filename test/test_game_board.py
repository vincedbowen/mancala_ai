from unittest import TestCase, mock
from unittest.mock import patch

from board.game_board import Board


class TestBoard(TestCase):
    def test_valid_move_basic(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 2,
            1: 1, 2: 0, 3: 4, 4: 8, 5: 6, 6: 0,
            'player 2 mancala': 3,
            7: 0, 8: 1, 9: 2, 10: 4, 11: 5, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.valid_move(3)
            self.assertTrue(result)

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.valid_move(2)
            self.assertFalse(result)

    def test_valid_move_edge_cases(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 2,
            1: 1, 2: 0, 3: 4, 4: 8, 5: 6, 6: 0,
            'player 2 mancala': 3,
            7: 0, 8: 1, 9: 2, 10: 4, 11: 5, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.valid_move(0)
            self.assertFalse(result)
        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.valid_move(7)
            self.assertFalse(result)
        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.valid_move(14)
            self.assertFalse(result)

    def test_player_two_pit_correction(self):
        board = Board()
        new_pit = board.player_two_pit_correction(4)
        self.assertEqual(new_pit, 10)

    def test_move(self):
        self.fail()

    def test_winning_eval_one_side_empty(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 5,
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
            'player 2 mancala': 4,
            7: 0, 8: 0, 9: 0, 10: 9, 11: 0, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.winning_eval()
            self.assertTrue(result)

    def test_winning_eval_both_sides_empty(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 30,
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
            'player 2 mancala': 18,
            7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.winning_eval()
            self.assertTrue(result)

    def test_winning_eval_neither_sides_empty(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 30,
            1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0,
            'player 2 mancala': 18,
            7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 3
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.winning_eval()
            self.assertFalse(result)

    def test_can_capture(self):
        self.fail()

    def test_capture(self):
        self.fail()

    def test_check_for_play_again(self):
        board = Board()
        board.move(4)
        self.assertEqual(board.current_player, 1)

    def test_determine_winner(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 5,
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
            'player 2 mancala': 4,
            7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.determine_winner()
            self.assertEqual(result, 1)

    def test_determine_winner_tie(self):
        board = Board()
        # Mocking player 1 winning
        mocked_state = {
            'player 1 mancala': 30,
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
            'player 2 mancala': 30,
            7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
        }

        with mock.patch.object(board, 'virtual_board', mocked_state):
            result = board.determine_winner()
            self.assertEqual(result, None)

    def test_switch_player(self):
        board = Board()
        mocked_state = 2
        with mock.patch.object(board, 'current_player', mocked_state):
            board.switch_player()
            self.assertEqual(board.current_player, 1)
            board.switch_player()
            self.assertEqual(board.current_player, 2)

