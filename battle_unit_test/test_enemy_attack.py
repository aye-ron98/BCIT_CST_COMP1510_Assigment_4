from unittest import TestCase
from unittest.mock import patch
from battle_mechanics import enemy_attack
import io


class TestEnemyAttack(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack(self, mock_print):
        actual = enemy_attack({'damage': 5, 'defence': 5, 'name': 'joe'}, 10, ('kick', 15))
        expect = 10
        the_game_printed_this = mock_print.getvalue()
        expected_output = "joe chose kick!\n" \
                          "joe dealt 10 damage to you!"
        self.assertEqual(expect, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_guard(self, mock_print):
        actual = enemy_attack({'damage': 5, 'defence': 5, 'name': 'joe'}, 10, ('roll', -15))
        expect = -15
        the_game_printed_this = mock_print.getvalue()
        expected_output = "joe chose roll!\n" \
                          "Your next attack will now do 15 less damage to joe!\n"
        self.assertEqual(expect, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_return_0(self, mock_print):
        actual = enemy_attack({'damage': 5, 'defence': 5, 'name': 'joe'}, 10, ('hit', 5))
        expect = 0
        the_game_printed_this = mock_print.getvalue()
        expected_output = "joe chose hit!\n" \
                          "joe dealt 0 damage to you!"
        self.assertEqual(expect, actual)
        self.assertEqual(expected_output, the_game_printed_this)
