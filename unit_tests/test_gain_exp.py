from unittest import TestCase

from game import gain_exp, \
    MAX_MAP_Y_LVL1, MAX_MAP_X_LVL1, MAX_MAP_Y_LVL2, MAX_MAP_X_LVL2, MAX_MAP_Y_LVL3, MAX_MAP_X_LVL3, \
    LVL2_EXP_OUTSET, LVL3_EXP_OUTSET, ILLUSIONIST_STATS_LVL1, ILLUSIONIST_STATS_LVL2


class TestGainExp(TestCase):

    def test_gain_exp_increases_character_EXP_by_experience_gain_passed(self):
        character = {"EXP": 0, "level": 1}
        board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
        expected = 100
        gain_exp(character, 100, board)
        self.assertEqual(expected, character["EXP"])

    def test_gain_exp_updates_EXP_and_level_when_level_2_outset_met(self):
        character = {"EXP": 100, "level": 1}
        character.update(ILLUSIONIST_STATS_LVL1())
        experience_gain = LVL2_EXP_OUTSET() - character["EXP"]
        board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
        gain_exp(character, experience_gain, board)
        expected = {"EXP": LVL2_EXP_OUTSET(), "level": 2}
        self.assertEqual(expected["level"], character["level"])
        self.assertEqual(MAX_MAP_X_LVL2(), board["max-x"])
        self.assertEqual(MAX_MAP_Y_LVL2(), board["max-y"])

    def test_gain_exp_updates_EXP_and_level_when_level_3_outset_met(self):
        character = {"EXP": LVL2_EXP_OUTSET(), "level": 2, "class": "Illusionist"}
        character.update(ILLUSIONIST_STATS_LVL2())
        experience_gain = LVL3_EXP_OUTSET() - character["EXP"]
        board = {"max-x": MAX_MAP_X_LVL2(), "max-y": MAX_MAP_Y_LVL2()}
        gain_exp(character, experience_gain, board)
        expected = {"EXP": LVL3_EXP_OUTSET(), "level": 3}
        self.assertEqual(expected["level"], character["level"])
        self.assertEqual(MAX_MAP_X_LVL3(), board["max-x"])
        self.assertEqual(MAX_MAP_Y_LVL3(), board["max-y"])
