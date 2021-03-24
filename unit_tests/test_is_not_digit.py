from unittest import TestCase

from game import is_not_digit


class TestIsNotDigit(TestCase):

    def test_is_not_digit_string_is_digit_character(self):
        actual = is_not_digit("6")
        self.assertFalse(actual)

    def test_is_not_digit_string_is_whitespace_character(self):
        actual = is_not_digit(" ")
        self.assertTrue(actual)

    def test_is_not_digit_string_is_uppercase_letter_character(self):
        actual = is_not_digit("N")
        self.assertTrue(actual)

    def test_is_not_digit_string_is_lowercase_letter_character(self):
        actual = is_not_digit("j")
        self.assertTrue(actual)

    def test_is_not_digit_string_is_punctuation_character(self):
        actual = is_not_digit("!")
        self.assertTrue(actual)

    def test_is_not_digit_string_is_special_character(self):
        actual = is_not_digit("~")
        self.assertTrue(actual)
