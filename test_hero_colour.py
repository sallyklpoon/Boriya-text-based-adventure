from unittest import TestCase
from game import hero_colour


class TestHeroColour(TestCase):

    def test_hero_colour_wraps_nonempty_string_in_cyan_ASCII(self):
        test_text = "Swimming!"
        expected = "\x1b[36mSwimming!\x1b[0m"
        actual = hero_colour(test_text)
        self.assertEqual(expected, actual)

    def test_hero_colour_wraps_empty_string_in_cyan_ASCII(self):
        test_text = ""
        expected = "\x1b[36m\x1b[0m"
        actual = hero_colour(test_text)
        self.assertEqual(expected, actual)

    def test_hero_colour_return_contains_same_text_passed(self):
        test_text = "Hello World"
        actual = hero_colour(test_text)
        self.assertTrue(test_text in actual)

    def test_hero_colour_return_contains_whitespace_special_characters(self):
        test_text = "$-A@ *"
        actual = hero_colour(test_text)
        self.assertTrue(test_text in actual)

    def test_hero_colour_is_not_text_passed(self):
        test_text = "Hello World"
        actual = hero_colour(test_text)
        self.assertNotEqual(test_text, actual)
