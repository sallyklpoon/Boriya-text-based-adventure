from unittest import TestCase
from unittest.mock import patch

from game import select_foe, \
    WEAK_FOE_1, WEAK_FOES, \
    STRONG_FOE_1, STRONG_FOE_2, STRONG_FOES, \
    EPIC_FOE_3, EPIC_FOES


class TestSelectFoe(TestCase):

    @patch('random.randint', return_value=2)
    def test_select_foe_returns_a_dict(self, mock_randint):
        expected_instance = dict
        actual = select_foe(STRONG_FOES())
        self.assertIsInstance(actual, expected_instance)

    @patch('random.randint', return_value=1)
    def test_select_foe_returns_weak_foe1_when_weak_foes_selection_and_roll_1(self, mock_randint):
        expected = WEAK_FOE_1()
        actual = select_foe(WEAK_FOES())
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_select_foe_returns_strong_foe2_when_strong_foes_selection_and_roll_2(self, mock_randint):
        expected = STRONG_FOE_2()
        actual = select_foe(STRONG_FOES())
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_select_foe_returns_epic_foe3_when_epic_foes_selection_and_roll_3(self, mock_randint):
        expected = EPIC_FOE_3()
        actual = select_foe(EPIC_FOES())
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_select_foe_returns_strong_foe_when_epic_foes_selection(self, mock_randint):
        expected = STRONG_FOE_1()
        actual = select_foe(STRONG_FOES())
        self.assertEqual(expected, actual)
