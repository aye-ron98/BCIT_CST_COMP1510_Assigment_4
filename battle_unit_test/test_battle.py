
from unittest import TestCase
from unittest.mock import patch
import io
from battle_mechanics import battle


class TestBattle(TestCase):

    @patch('battle_mechanics.battle_cards', return_value=(('kick', 1), ('stand', -1)))
    @patch('battle_mechanics.battle_cards', return_value=(('finisher', 100), ('guard', 2)))
    @patch('random.randint', return_value=1)
    @patch('enemy.additional_enemy_characteristics', side_effect=None)
    @patch('battle_mechanics.player_attack', return_value=100)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_player_win(self, mock_print, mock_attack, mock_characteristics, mock_roll, mock_enemy, mock_player):
        actual = battle({'hp': 100, 'defence': 5, 'damage': 100, 'xp': 1},
                        {'hp': 10, 'defence': 0, 'damage': 2, 'name': 'bob'}, True)
        expected = '\nYou should know, bob is planning to use stand on you!\n' \
                   'bob has been defeated! You gain 1 xp. You are at 100 health.\n' \
                   '\nthe battle is over! You are now at 100 health\n'
        the_game_printed_this = mock_print.getvalue()
        self.assertEqual({'damage': 100, 'defence': 5, 'hp': 100, 'xp': 2}, actual)
        self.assertEqual(expected, the_game_printed_this)

    @patch('battle_mechanics.battle_cards', return_value=(('finisher', 100), ('guard', -5)))
    @patch('battle_mechanics.battle_cards', return_value=(('penultimate', 100), ('stand', -1)))
    @patch('enemy.additional_enemy_characteristics', side_effect=None)
    @patch('battle_mechanics.enemy_attack', return_value=100)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_player_loose(self, mock_print, mock_attack, mock_characteristics, mock_enemy, mock_player):
        actual = battle({'hp': 100, 'defence': 0, 'damage': 100, 'xp': 1},
                        {'hp': 10, 'defence': 0, 'damage': 2, 'name': 'bob'}, False)
        expected = 'You are now at 0 health!\nYou are defeated\n'
        the_game_printed_this = mock_print.getvalue()
        self.assertEqual({'damage': 100, 'defence': 0, 'hp': 0, 'moves': (('finisher', 100),
                                                                          ('guard', -5)), 'xp': 1}, actual)
        self.assertEqual(expected, the_game_printed_this)
