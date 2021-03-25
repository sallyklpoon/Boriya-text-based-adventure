import io
from unittest import TestCase
from unittest.mock import patch

from game import start_game, START_GAME_MSG, PROLOGUE


class TestStartGame(TestCase):

    @patch('builtins.input', side_effect=["Bob", "1"])
    def test_start_game_returns_tuple(self, mock_input):
        expected_instance = tuple
        actual = start_game()
        self.assertIsInstance(actual, expected_instance)

    @patch('builtins.input', side_effect=["Beepboops", "2"])
    def test_start_game_returns_tuple_containing_two_dictionaries(self, mock_input):
        expected_instance = dict
        actual = start_game()
        for element in actual:
            self.assertIsInstance(element, expected_instance)

    @patch('builtins.input', side_effect=["Gabriel", "3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_prints_start_game_msg(self, mock_sys, mock_input):
        start_game()
        actual_output = mock_sys.getvalue()
        self.assertIn(START_GAME_MSG(), actual_output)

    @patch('builtins.input', side_effect=["Fluffy Boi", "4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_prints_prologue(self, mock_sys, mock_input):
        start_game()
        actual_output = mock_sys.getvalue()
        self.assertIn(PROLOGUE(), actual_output)