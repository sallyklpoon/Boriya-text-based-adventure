from unittest import TestCase
from unittest.mock import patch

from game import make_character, START_X, START_Y, \
    CHARACTER_START_LEVEL, CHARACTER_START_EXP, \
    ILLUSIONIST_STATS_LVL1, ROGUE_STATS_LVL1, RANGER_STATS_LVL1, PALADIN_STATS_LVL1


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=["Sally", "2"])
    def test_make_character_returns_dictionary(self, mock_input):
        expected_instance = dict
        actual = make_character()
        self.assertIsInstance(actual, expected_instance)

    @patch('builtins.input', side_effect=["Ikki Ooli", "1"])
    def test_make_character_dictionary_contains_necessary_keys(self, mock_input):
        expected = {"name": "\033[36mIkki Ooli\033[0m", "x-location": START_X(),
                    "y-location": START_Y(), "EXP": CHARACTER_START_EXP(),
                    "level": CHARACTER_START_LEVEL(), "quit": False}
        expected.update(ILLUSIONIST_STATS_LVL1())
        expected['attacks'] = ["\033[36mColour Spray\033[0m",
                               "\033[36mPhantasmal Force\033[0m",
                               "\033[36mShadow Blade\033[0m"]
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Sally! !", "2"])
    def test_make_character_dictionary_some_name_class_option_2(self, mock_input):
        expected = {"name": "\033[36mSally! !\033[0m", "x-location": START_X(),
                    "y-location": START_Y(), "EXP": CHARACTER_START_EXP(),
                    "level": CHARACTER_START_LEVEL(), "quit": False}
        expected.update(ROGUE_STATS_LVL1())
        expected['attacks'] = ["\033[36mSneak Attack\033[0m",
                               "\033[36mtheir Dagger\033[0m",
                               "\033[36mtheir Hand-Crossbow\033[0m"]
        expected['HP'] = expected['max-HP']
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Marti", "3"])
    def test_make_character_dictionary_some_name_class_option_3(self, mock_input):
        expected = {"name": "\033[36mMarti\033[0m", "x-location": START_X(),
                    "y-location": START_Y(), "EXP": CHARACTER_START_EXP(),
                    "level": CHARACTER_START_LEVEL(), "quit": False}
        expected.update(RANGER_STATS_LVL1())
        expected['attacks'] = ["\033[36mEnsnaring Strike\033[0m",
                               "\033[36mHail of Thorns\033[0m",
                               "\033[36mThorn Whip\033[0m"]
        expected['HP'] = expected['max-HP']
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["~~Jake", "4"])
    def test_make_character_dictionary_some_name_class_option_4(self, mock_input):
        expected = {"name": "\033[36m~~Jake\033[0m", "x-location": START_X(),
                    "y-location": START_Y(), "EXP": CHARACTER_START_EXP(),
                    "level": CHARACTER_START_LEVEL(), "quit": False}
        expected.update(PALADIN_STATS_LVL1())
        expected['attacks'] = ["\033[36mBranding Smite\033[0m",
                               "\033[36mThunderous Smite\033[0m",
                               "\033[36mShield Bash\033[0m"]
        expected['HP'] = expected['max-HP']
        actual = make_character()
        self.assertEqual(expected, actual)
