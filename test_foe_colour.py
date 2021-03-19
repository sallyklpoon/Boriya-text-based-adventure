from unittest import TestCase
from game import foe_colour


class TestFoeColour(TestCase):

    def test_hero_colour_wraps_nonempty_string_in_cyan_ASCII(self):
        test_text = "Swimming!"
        expected = "\x1b[33mSwimming!\x1b[0m"
        actual = foe_colour(test_text)
        self.assertEqual(expected, actual)

    def test_hero_colour_wraps_empty_string_in_cyan_ASCII(self):
        test_text = ""
        expected = "\x1b[33m\x1b[0m"
        actual = foe_colour(test_text)
        self.assertEqual(expected, actual)

    def test_hero_colour_return_contains_same_text_passed(self):
        test_text = "Hello World"
        actual = foe_colour(test_text)
        self.assertTrue(test_text in actual)

    def test_hero_colour_return_contains_whitespace_special_characters(self):
        test_text = "$-A@ *"
        actual = foe_colour(test_text)
        self.assertTrue(test_text in actual)

    def test_hero_colour_is_not_text_passed(self):
        test_text = "Hello World"
        actual = foe_colour(test_text)
        self.assertNotEqual(test_text, actual)
