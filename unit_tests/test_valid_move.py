from unittest import TestCase

from game import valid_move


class TestValidMove(TestCase):

    def test_valid_move_character_can_move_north_at_middle_of_board(self):
        board = {"max-x": 40, "max-y": 40}
        actual = valid_move("1", board["max-x"] // 2, board["max-x"] // 2, board)
        self.assertTrue(actual)

    def test_valid_move_character_can_move_south_at_middle_of_board(self):
        board = {"max-x": 10, "max-y": 33}
        actual = valid_move("2", board["max-x"] // 2, board["max-x"] // 2, board)
        self.assertTrue(actual)

    def test_valid_move_character_can_move_east_at_middle_of_board(self):
        board = {"max-x": 25, "max-y": 25}
        actual = valid_move("3", board["max-x"] // 2, board["max-x"] // 2, board)
        self.assertTrue(actual)

    def test_valid_move_character_can_move_west_at_middle_of_board(self):
        board = {"max-x": 50, "max-y": 50}
        actual = valid_move("4", board["max-x"] // 2, board["max-x"] // 2, board)
        self.assertTrue(actual)

    def test_valid_move_character_cannot_move_on_board_1x1(self):
        board = {"max-x": 1, "max-y": 1}
        actual = valid_move("1", 0, 0, board)
        self.assertFalse(actual)

    def test_valid_move_character_cannot_move_north_at_y0(self):
        board = {"max-x": 2, "max-y": 5}
        actual = valid_move("1", 1, 0, board)
        self.assertFalse(actual)

    def test_valid_move_character_cannot_move_east_at_x0(self):
        board = {"max-x": 8, "max-y": 10}
        actual = valid_move("3", 0, 6, board)
        self.assertFalse(actual)

    def test_valid_move_character_cannot_move_south_at_board_max_y(self):
        board = {"max-x": 50, "max-y": 89}
        actual = valid_move("2", 15, board["max-y"], board)
        self.assertFalse(actual)

    def test_valid_move_character_cannot_move_west_at_board_max_x(self):
        board = {"max-x": 32, "max-y": 65}
        actual = valid_move("4", board["max-x"], 37, board)
        self.assertFalse(actual)
