from unittest import TestCase

from game import format_character, hero_colour, foe_colour


class TestFormatCharacter(TestCase):

    def test_format_character_formats_empty_strings(self):
        foe = {"name": "", "attacks": ["", ""]}
        expected = {"name": "\033[33m\033[0m", "attacks": ["\033[33m\033[0m", "\033[33m\033[0m"]}
        format_character(format_style=foe_colour, character=foe)
        self.assertEqual(expected, foe)

    def test_format_character_formats_non_empty_strings_with_foe_colour(self):
        foe = {"name": "Samir", "attacks": ["Jump", "Dance"]}
        expected = {"name": "\033[33mSamir\033[0m", "attacks": ["\033[33mJump\033[0m", "\033[33mDance\033[0m"]}
        format_character(format_style=foe_colour, character=foe)
        self.assertEqual(expected, foe)

    def test_format_character_formats_non_empty_strings_with_hero_colour(self):
        hero = {"name": "Florence", "attacks": ["Eat", "Sleep"]}
        expected = {"name": "\033[36mFlorence\033[0m", "attacks": ["\033[36mEat\033[0m", "\033[36mSleep\033[0m"]}
        format_character(format_style=hero_colour, character=hero)
        self.assertEqual(expected, hero)
