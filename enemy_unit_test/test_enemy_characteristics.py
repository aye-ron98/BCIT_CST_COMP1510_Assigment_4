from unittest import TestCase
from unittest.mock import patch
from enemy import additional_enemy_characteristics
import io


class TestEnemyCharacteristic(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_additional_enemy_characteristics_no_print(self, mock_print):
        additional_enemy_characteristics({'damage': 0, 'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_additional_enemy_characteristics_print_damage(self, mock_print):
        additional_enemy_characteristics({'damage': 1, 'defence': 0, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "Watch out! jerry has been hitting the gym! All their attacks will have a +1 effect!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_additional_enemy_characteristics_print_defence(self, mock_print):
        additional_enemy_characteristics({'damage': 0, 'defence': 1, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "jerry has been meditating lately, all your attacks will have a -1 effect!\n"
        self.assertEqual(expected_output, the_game_printed_this)
