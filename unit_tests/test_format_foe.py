from unittest import TestCase

from game import format_foe


class TestFormatFoe(TestCase):

    def test_format_foe_formats_empty_strings(self):
        foe = {"name": "", "attacks": ["", ""]}
        expected = {"name": "\033[33m\033[0m", "attacks": ["\033[33m\033[0m", "\033[33m\033[0m"]}
        format_foe(foe)
        self.assertEqual(expected, foe)

    def test_format_foe_formats_non_empty_strings(self):
        foe = {"name": "Samir", "attacks": ["Jump", "Dance"]}
        expected = {"name": "\033[33mSamir\033[0m", "attacks": ["\033[33mJump\033[0m", "\033[33mDance\033[0m"]}
        format_foe(foe)
        self.assertEqual(expected, foe)
