from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetClassChoice(TestCase):

    @patch('builtins.input', result="3")
    def test_get_user_choice_returns_input(self, mock_input):
        expected = "3"
        actual = get_user_choice("something")
        self.assertTrue(actual, expected)
