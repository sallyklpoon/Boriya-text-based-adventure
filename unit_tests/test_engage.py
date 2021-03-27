from unittest import TestCase
from unittest.mock import patch

from game import engage


class TestEngage(TestCase):

    @patch('builtins.input', return_value="1")
    def test_engage_returns_true_if_user_inputs_1_to_attack(self, mock_input):
        actual = engage()
        self.assertTrue(actual)

    @patch('builtins.input', return_value="2")
    def test_engage_returns_false_if_user_inputs_2_to_flee(self, mock_input):
        actual = engage()
        self.assertFalse(actual)
