import io
from unittest import TestCase
from unittest.mock import patch

from game import get_menu


class TestGetMenu(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_menu_move(self, mock_output):
        get_menu("move")
        expected_output = "\n[1] go North\n[2] go South\n[3] go West\n[4] go East\n[5] Quit Game\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_menu_engage(self, mock_output):
        get_menu("engage")
        expected_output = "\n[1] Attack\n[2] Flee\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_menu_class(self, mock_output):
        get_menu("class")
        expected_output = "\n[1] Illusionist\n[2] Rogue\n[3] Ranger\n[4] Paladin\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
