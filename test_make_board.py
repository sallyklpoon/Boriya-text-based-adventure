from unittest import TestCase

from game import make_board


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

    def test_make_board_lvl_1_includes_coordinates_in_lvl_1(self):
        actual = make_board(1)
