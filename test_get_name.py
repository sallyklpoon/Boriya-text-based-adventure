from unittest import TestCase
from unittest.mock import patch

from game import get_name


class TestGetName(TestCase):

    @patch('builtins.input', result="")
    def test_get_name_returns_empty_input(self, mock_input):
        expected = ""
        actual = get_name()
        self.assertTrue(actual, expected)

    @patch('builtins.input', result="1. Sally & Martin!")
    def test_get_name_returns_string_with_mix_characters_input(self, mock_input):
        expected = "1. Sally & Martin!"
        actual = get_name()
        self.assertTrue(actual, expected)
