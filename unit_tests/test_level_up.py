from unittest import TestCase

from game import level_up, \
    MAX_MAP_X_LVL1, MAX_MAP_Y_LVL1, MAX_MAP_X_LVL2, MAX_MAP_Y_LVL2, MAX_MAP_X_LVL3, MAX_MAP_Y_LVL3, \
    ILLUSIONIST_STATS_LVL2, hero_colour, PALADIN_STATS_LVL3


class TestLevelUp(TestCase):

    def test_level_up_levels_up_game_to_level_2(self):
        character = {"level": 1, "class": "Rogue"}
        board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
        level_up(character, board)
        expected_level = 2
        self.assertEqual(expected_level, character["level"])       # Character levelled up
        self.assertTrue(board["max-x"] == MAX_MAP_X_LVL2()
                        and board["max-y"] == MAX_MAP_Y_LVL2())    # Map levelled up to lvl 2

    def test_level_up_levels_up_game_to_level_3(self):
        character = {"level": 2, "class": "Rogue"}
        board = {"max-x": MAX_MAP_X_LVL2(), "max-y": MAX_MAP_Y_LVL2()}
        level_up(character, board)
        expected_level = 3
        self.assertEqual(expected_level, character["level"])       # Character levelled up
        self.assertTrue(board["max-x"] == MAX_MAP_X_LVL3()
                        and board["max-y"] == MAX_MAP_Y_LVL3())    # Map levelled up to lvl 3

    def test_level_up_levels_up_correct_class_lvl1_Illusionist_to_lvl2_Illusionist(self):
        character = {"class": "Illusionist", "level": 1}
        board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
        level_up(character, board)
        expected = {"level": 2, "class": "Illusionist"}
        expected.update(ILLUSIONIST_STATS_LVL2())
        expected["attacks"] = list(map(hero_colour, expected["attacks"]))
        self.assertEqual(expected, character)

    def test_level_up_levels_up_correct_class_lvl2_Paladin_to_lvl3_Paladin(self):
        character = {"class": "Paladin", "level": 2}
        board = {"max-x": MAX_MAP_X_LVL2(), "max-y": MAX_MAP_Y_LVL2()}
        level_up(character, board)
        expected = {"level": 3, "class": "Paladin"}
        expected.update(PALADIN_STATS_LVL3())
        expected["attacks"] = list(map(hero_colour, expected["attacks"]))
        self.assertEqual(expected, character)
