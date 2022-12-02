from unittest import TestCase
from unittest.mock import patch
from scenarios import add_health
import io


class TestAddHealth(TestCase):

    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_zero_heath_gain(self, mock_print, _):
        actual = add_health({'hp': 10})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou come across a hospital, advertisers feed you a lot of " \
                          "multivitamins, you gain 0 health\n"
        self.assertEqual(actual, {'hp': 10})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure(self, mock_print, _):
        actual = add_health({'hp': 10})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou come across a hospital, advertisers feed you a lot of " \
                          "multivitamins, you gain 2 health\n"
        self.assertEqual(actual, {'hp': 12})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_max_heath_gain(self, mock_print, _):
        actual = add_health({'hp': 10})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou come across a hospital, advertisers feed you a lot of " \
                          "multivitamins, you gain 4 health\n"
        self.assertEqual(actual, {'hp': 14})
        self.assertEqual(expected_output, the_game_printed_this)
