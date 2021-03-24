from unittest import TestCase
from unittest.mock import patch

from game import get_class_choice


class TestGetClassChoice(TestCase):

    @patch('builtins.input', result="3")
    def test_get_class_choice_returns_input(self, mock_input):
        expected = "3"
        actual = get_class_choice()
        self.assertTrue(actual, expected)

