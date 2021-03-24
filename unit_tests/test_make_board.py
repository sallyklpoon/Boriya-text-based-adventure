from unittest import TestCase

from game import make_board, \
    MAX_MAP_X_LVL1, MAX_MAP_Y_LVL1, \
    MAX_MAP_X_LVL2, MAX_MAP_Y_LVL2, \
    MAX_MAP_X_LVL3, MAX_MAP_Y_LVL3


class TestMakeBoard(TestCase):

    def test_make_board_keys_are_coordinate_tuples_or_maxX_maxY(self):
        actual = make_board(1)
        for key in actual.keys():
            self.assertTrue(key == "max-x" or key == "max-y" or tuple)

    def test_make_board_maxX_is_int(self):
        expected_instance = int
        actual = make_board(2)
        self.assertIsInstance(actual['max-x'], expected_instance)

    def test_make_board_maxY_is_int(self):
        expected_instance = int
        actual = make_board(3)
        self.assertIsInstance(actual['max-y'], expected_instance)

    def test_make_board_tuple_keys_contain_int(self):
        expected_instance = int
        actual = make_board(2)
        for key in actual.keys():
            if key is tuple:
                for element in key:
                    self.assertIsInstance(element, expected_instance)

    def test_make_board_coordinate_keys_have_string_values(self):
        expected_instance = str
        actual = make_board(2)
        for key in actual.keys():
            if key is tuple:
                self.assertIsInstance(actual[key], expected_instance)

    def test_make_board_lvl_1_includes_coordinates_defined_for_lvl_1(self):
        actual = make_board(1)
        for key in actual.keys():
            if key is tuple:
                self.assertTrue(key[0] in range(MAX_MAP_X_LVL1()) and
                                key[1] in range(MAX_MAP_Y_LVL1()))

    def test_make_board_lvl_2_includes_coordinates_defined_for_lvl_2(self):
        actual = make_board(2)
        for key in actual.keys():
            if key is tuple:
                self.assertTrue(key[0] in range(MAX_MAP_X_LVL2()) and
                                key[1] in range(MAX_MAP_Y_LVL2()))

    def test_make_board_lvl_3_includes_coordinates_defined_for_lvl_3(self):
        actual = make_board(3)
        for key in actual.keys():
            if key is tuple:
                self.assertTrue(key[0] in range(MAX_MAP_X_LVL3()) and
                                key[1] in range(MAX_MAP_Y_LVL3()))
