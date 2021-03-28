import io
from unittest import TestCase
from unittest.mock import patch

from game import end_game, GOAL_LOCATION


class TestEndGame(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_prints_message_if_character_dead(self, mock_output):
        character = {"name": "James", "HP": 0, "x-location": 2, "y-location": 4, "quit": False}
        expected = f"\n༺═────────────────────────────────────────────────────────────────────────────────────────═༻\n"\
                   f"\n" \
                   f"Falling down to the cold ground, you feel your soul slowly being devoured by the darkness " \
                   f"around you.\nAs you breathe your last breath, you see a sliver of moonlight appear in the sky " \
                   f"above you, \nbut it only lasts for an instant, before being swallowed by the infinite " \
                   f"nothingness around you.\n\nGoodbye, {character['name']}.\n"\
                   f"\n༺═────────────────────────────────────────────────────────────────────────────────────────═༻" \
                   f"\n\nThank you for playing, {character['name']}! - Marti & Sally\n"
        end_game(character)
        actual_output = mock_output.getvalue()
        self.assertEqual(expected, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_message_if_character_kills_boss(self, mock_output):
        character = {"name": "James", "HP": 12,
                     "x-location": GOAL_LOCATION()[0], "y-location": GOAL_LOCATION()[1], "quit": False}
        expected = f"\n༺═────────────────────────────────────────────────────────────────────────────═༻\n"\
                   f"\nAs you look down at Erebus' lifeless body, you see an inkling of light appear through \n"\
                   f"the darkened clouds above. You feel the blight slowly leave the forest, as the moonlight\n"\
                   f"begins to pour in through the shadows. Your journey has finally come to an end.\n"\
                   f"\nMay you rest easy now, {character['name']}, the Forest of Bóriya is finally rid of its\n"\
                   f"blight.\n"\
                   f"\n༺═────────────────────────────────────────────────────────────────────────────═༻\n" \
                   f"\n\nThank you for playing, {character['name']}! - Marti & Sally\n"
        end_game(character)
        actual_output = mock_output.getvalue()
        self.assertEqual(expected, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_message_if_character_quits(self, mock_output):
        character = {"name": "James", "HP": 12,
                     "x-location": GOAL_LOCATION()[0]+3, "y-location": GOAL_LOCATION()[1]-1, "quit": True}
        expected = f"\n༺═──────────────────────────────────────────────────═༻\n"\
                   f"The Forest of Bóriya has taken it's toll on your soul.\n"\
                   f"You can no longer continue. Goodbye, {character['name']}.\n"\
                   f"༺═──────────────────────────────────────────────────═༻\n" \
                   f"\nThank you for playing, {character['name']}! - Marti & Sally\n"
        end_game(character)
        actual_output = mock_output.getvalue()
        self.assertEqual(expected, actual_output)
