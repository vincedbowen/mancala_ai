from unittest import mock
from unittest import TestCase
from userInput import user_input


class TestUserInput(TestCase):
    @mock.patch('userInput.user_input.input', create=True)
    def test_get_pit(self, mock_input):
        mock_input.side_effect = ['j', '1.4', '2.77', '3']
        result = user_input.get_pit()
        self.assertEqual(result, 3)

    @mock.patch('userInput.user_input.input', create=True)
    def test_get_turn_num(self, mock_input):
        mock_input.side_effect = ['test', '1', '2.77', 'y']
        result = user_input.get_turn_num()
        self.assertEqual(result, 'y')

    @mock.patch('userInput.user_input.input', create=True)
    def test_get_file_option(self, mock_input):
        mock_input.side_effect = ['test', '4', '0.1', '2']
        result = user_input.get_option()
        self.assertEqual(result, "play.py")

    @mock.patch('userInput.user_input.input', create=True)
    def test_get_num_sims(self, mock_input):
        mock_input.side_effect = ['string', '99.5', '101', '99']
        result = user_input.get_num_sims()
        self.assertEqual(result, 99)