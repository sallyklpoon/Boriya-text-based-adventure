import io
from unittest import TestCase
from unittest.mock import patch

from game import print_map


class TestPrintMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_character_at_0_0_board_dimensions_1_1(self, mock_output):
        sample_character = {"x-location": 0, "y-location": 0}
        sample_board = {"max-x": 1, "max-y": 1}
        expected = "[\033[36m웃\033[0m]\n"
        print_map(sample_character, sample_board)
        actual_output = mock_output.getvalue()
        self.assertEqual(actual_output, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_character_at_middle_of_board_dimensions_3_3(self, mock_output):
        sample_character = {"y-location": 1, "x-location": 1, "some-key": "ABC"}
        sample_board = {"max-x": 3, "max-y": 3, (0, 0): "anything here"}
        expected = "[  ][  ][  ]\n[  ][\033[36m웃\033[0m][  ]\n[  ][  ][  ]\n"
        print_map(sample_character, sample_board)
        actual_output = mock_output.getvalue()
        self.assertEqual(actual_output, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_character_at_bottom_row_last_column_of_board_dimensions_4_4(self, mock_output):
        sample_character = {"x-location": 3, "some-key": "ABC", "y-location": 3}
        sample_board = {"max-y": 4, "pies": "they're tasty!", "max-x": 4, }
        expected = "[  ][  ][  ][  ]\n[  ][  ][  ][  ]\n[  ][  ][  ][  ]\n[  ][  ][  ][\033[36m웃\033[0m]\n"
        print_map(sample_character, sample_board)
        actual_output = mock_output.getvalue()
        self.assertEqual(actual_output, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_contains_character_in_room_representation(self, mock_output):
        sample_character = {"x-location": 14, "y-location": 8}
        sample_board = {"max-x": 25, "max-y": 25, (0, 0): "anything here"}
        expected_character_rep = "[\033[36m웃\033[0m]"
        print_map(sample_character, sample_board)
        actual_output = mock_output.getvalue()
        self.assertIn(expected_character_rep, actual_output)
