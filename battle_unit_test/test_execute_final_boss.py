from unittest import TestCase
from unittest.mock import patch
from battle_mechanics import execute_final_boss
import io


class TestExecuteFinalBoss(TestCase):

    @patch('battle_mechanics.battle', return_value={'hp': 10, 'name': 'hero', 'damage': 10, 'defence': 10})
    @patch('battle_mechanics.roll_initaitve', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_final_boss(self, mock_print, mock_roll,  mock_battle):
        actual = execute_final_boss({'hp': 100, 'name': 'hero', 'damage': 0, 'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nWhat out hero, its the final boss!To help you out you are " \
                          "getting a power buff, +20 health, +10 attack, +10 defense\n"
        self.assertEqual({'hp': 10, 'name': 'hero', 'damage': 10, 'defence': 10}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('battle_mechanics.battle', return_value={'hp': 10, 'name': 'hero', 'damage': 10, 'defence': 10})
    @patch('battle_mechanics.roll_initaitve', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_final_boss_hero_goes_second(self, mock_print, mock_roll, mock_battle):
        actual = execute_final_boss({'hp': 100, 'name': 'hero', 'damage': 0, 'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nWhat out hero, its the final boss!To help you out you are getting a power buff, " \
                          "+20 health, +10 attack, +10 defense\n"
        self.assertEqual({'hp': 10, 'name': 'hero', 'damage': 10, 'defence': 10}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('battle_mechanics.battle', return_value={'hp': 0, 'name': 'hero', 'damage': 10, 'defence': 10})
    @patch('battle_mechanics.roll_initaitve', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_final_boss_hero_loose(self, mock_print, mock_roll, mock_battle):
        actual = execute_final_boss({'hp': 100, 'name': 'hero', 'damage': 0, 'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nWhat out hero, its the final boss!To help you out you are getting a power buff, " \
                          "+20 health, +10 attack, +10 defense\n"
        self.assertEqual({'hp': 0, 'name': 'hero', 'damage': 10, 'defence': 10}, actual)
        self.assertEqual(expected_output, the_game_printed_this)