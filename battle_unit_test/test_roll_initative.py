from unittest import TestCase
from unittest.mock import patch
from battle_mechanics import roll_initaitve
import io


class TestRollIniative(TestCase):

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_initaitve_True(self, mock_print, _):
        actual = roll_initaitve()
        expected = '\nYou are lucky today, you will attack first!\n'
        the_game_printed_this = mock_print.getvalue()
        self.assertEqual(True, actual)
        self.assertEqual(expected, the_game_printed_this)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_initaitve_False(self, mock_print, _):
        actual = roll_initaitve()
        expected = '\nnot so lucky, your enemy will attack first!\n'
        the_game_printed_this = mock_print.getvalue()
        self.assertEqual(False, actual)
        self.assertEqual(expected, the_game_printed_this)
