from unittest import TestCase
from unittest.mock import patch

from game import get_valid_input


class TestGetValidInput(TestCase):

    @patch('builtins.input', side_effect=["3"])
    def test_get_valid_input_user_enters_an_integer_aka_valid_input(self, mock_input):
        sample_menu = ("Cheese", "Vanilla", "Confetti", "Tiramisu", "Mango")
        actual = get_valid_input('cake', sample_menu)
        self.assertEqual(actual, "3")

    @patch('builtins.input', side_effect=["", "a", "Z", "#", "Hello!", "[4]", " 3 ", "2"])
    def test_get_valid_input_eventual_valid_input(self, mock_input):
        sample_menu = ("Orange", "Apple", "Peach")
        actual = get_valid_input('fruit', sample_menu)
        self.assertEqual(actual, "2")
