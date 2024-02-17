from unittest import mock
from unittest import TestCase
import user_pit

class Test(TestCase):
    @mock.patch('user_pit.input', create=True)
    def test_get_pit(self, mock_input):
        mock_input.side_effect = ['j', '1.4', '2.77', '3']
        result = user_pit.get_pit()
        self.assertEqual(result, 3)
