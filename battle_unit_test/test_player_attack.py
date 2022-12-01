from unittest import TestCase
from unittest.mock import patch
from battle_mechanics import player_attack
import io


class TestPlayerAttack(TestCase):

    @patch('movment.validate_move', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack(self, mock_print, mock_input):
        actual = player_attack({'hp': 10, 'damage': 5, 'defence': 0, 'moves': (('kick', 5), ('push', 2))}, -5)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "Quickly! To battle!\n" \
                          "\n1 kick\n" \
                          "2 push\n" \
                          "You chose kick and dealt 5 damage."
        self.assertEqual(5, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('movment.validate_move', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_player_10_damage(self, mock_print, mock_input):
        actual = player_attack({'hp': 10, 'damage': 5, 'defence': 0, 'moves': (('kick', 10), ('push', 2))}, -5)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "Quickly! To battle!\n" \
                          "\n1 kick\n" \
                          "2 push\n" \
                          "You chose kick and dealt 10 damage."
        self.assertEqual(10, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('movment.validate_move', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_player_0_damage(self, mock_print, mock_input):
        actual = player_attack({'hp': 10, 'damage': 5, 'defence': 0, 'moves': (('kick', 5), ('push', 2))}, -10)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "Quickly! To battle!\n" \
                          "\n1 kick\n" \
                          "2 push\n" \
                          "You chose push and dealt 0 damage."
        self.assertEqual(0, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('movment.validate_move', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_player_guard(self, mock_print, mock_input):
        actual = player_attack({'hp': 10, 'damage': 5, 'defence': 0, 'moves': (('kick', 5), ('guard', -2))}, -10)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "Quickly! To battle!\n" \
                          "\n1 kick\n" \
                          "2 guard\n" \
                          "You chose guard, the next attack will deal 2 less damage!\n"
        self.assertEqual(-2, actual)
        self.assertEqual(expected_output, the_game_printed_this)
