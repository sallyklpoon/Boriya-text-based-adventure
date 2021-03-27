from unittest import TestCase
from unittest.mock import patch

from game import next_move


class TestNextMove(TestCase):

    @patch('builtins.input', side_effect=["1", "3", "2"])
    def test_next_move_character_at_0_0_can_move_south(self, mock_inputs):
        board = {"max-x": 3, "max-y": 3}
        character = {"x-location": 0, "y-location": 0}
        expected = {"x-location": 0, "y-location": 1}
        next_move(character, board)
        self.assertEqual(character, expected)

    @patch('builtins.input', side_effect=["1", "3", "4"])
    def test_next_move_character_at_0_0_can_move_west(self, mock_inputs):
        board = {"max-x": 12, "max-y": 20}
        character = {"x-location": 0, "y-location": 0}
        expected = {"x-location": 1, "y-location": 0}
        next_move(character, board)
        self.assertEqual(character, expected)

    @patch('builtins.input', side_effect=["2", "4", "1"])
    def test_next_move_character_at_max_x_and_max_y_can_move_north(self, mock_inputs):
        board = {"max-x": 25, "max-y": 25}
        character = {"x-location": board['max-x'] - 1, "y-location": board['max-y'] - 1}
        expected = {"x-location": 24, "y-location": 23}
        next_move(character, board)
        self.assertEqual(character, expected)

    @patch('builtins.input', side_effect=["2", "4", "3"])
    def test_next_move_character_at_max_x_and_max_y_can_move_east(self, mock_inputs):
        board = {"max-x": 72, "max-y": 102}
        character = {"x-location": board['max-x'] - 1, "y-location": board['max-y'] - 1}
        expected = {"x-location": 70, "y-location": 101}
        next_move(character, board)
        self.assertEqual(character, expected)
