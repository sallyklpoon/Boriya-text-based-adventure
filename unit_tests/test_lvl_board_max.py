from unittest import TestCase

from game import lvl_board_max, \
    MAX_MAP_X_LVL1, MAX_MAP_Y_LVL1, \
    MAX_MAP_X_LVL2, MAX_MAP_Y_LVL2, \
    MAX_MAP_X_LVL3, MAX_MAP_Y_LVL3


class TestLvlBoardMax(TestCase):

    def test_lvl_board_max_returns_tuple(self):
        expected_type = tuple
        actual_return = lvl_board_max(1)
        self.assertIsInstance(actual_return, expected_type)

    def test_lvl_board_max_tuple_contains_int(self):
        expected_type = int
        actual_return = lvl_board_max(2)
        for element in actual_return:
            self.assertIsInstance(element, expected_type)

    def test_lvl_board_max_level_1(self):
        expected = (MAX_MAP_X_LVL1(), MAX_MAP_Y_LVL1())
        actual = lvl_board_max(1)
        self.assertEqual(expected, actual)

    def test_lvl_board_max_level_2(self):
        expected = (MAX_MAP_X_LVL2(), MAX_MAP_Y_LVL2())
        actual = lvl_board_max(2)
        self.assertEqual(expected, actual)

    def test_lvl_board_max_level_3(self):
        expected = (MAX_MAP_X_LVL3(), MAX_MAP_Y_LVL3())
        actual = lvl_board_max(3)
        self.assertEqual(expected, actual)

