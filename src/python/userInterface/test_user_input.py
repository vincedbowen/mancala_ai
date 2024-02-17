from unittest import mock
from unittest import TestCase
import user_input


class Test(TestCase):
    @mock.patch('user_input.input', create=True)
    def test_get_pit(self, mock_input):
        mock_input.side_effect = ['j', '1.4', '2.77', '3']
        result = user_input.get_pit()
        self.assertEqual(result, 3)

    @mock.patch('user_input.input', create=True)
    def test_get_turn_num(self, mock_input):
        mock_input.side_effect = ['test', '1', '2.77', 'y']
        result = user_input.get_turn_num()
        self.assertEqual(result, 'y')
