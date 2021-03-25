from unittest import TestCase

from game import move_character


class TestMoveCharacter(TestCase):

    def test_move_character_north(self):
        character = {"x-location": 5, "y-location": 2}
        expected = {"x-location": 5, "y-location": 1}
        move_character("1", character)
        self.assertEqual(character, expected)

    def test_move_character_south(self):
        character = {"x-location": 24, "y-location": 60}
        expected = {"x-location": 24, "y-location": 61}
        move_character("2", character)
        self.assertEqual(character, expected)

    def test_move_character_east(self):
        character = {"x-location": 33, "y-location": 9}
        expected = {"x-location": 32, "y-location": 9}
        move_character("3", character)
        self.assertEqual(character, expected)

    def test_move_character_west(self):
        character = {"x-location": 0, "y-location": 8}
        expected = {"x-location": 1, "y-location": 8}
        move_character("4", character)
        self.assertEqual(character, expected)


