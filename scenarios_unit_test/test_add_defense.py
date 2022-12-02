from unittest import TestCase
from scenarios import add_defense
from unittest.mock import patch
import io


class TestAddDefense(TestCase):

    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_zero_defence_gain(self, mock_print, _):
        actual = add_defense({'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou stubmle across an antique shop and leave with a " \
                          "stick shield, all attacks are now reduced by 0\n"
        self.assertEqual(actual, {'defence': 0})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_add_defence(self, mock_print, _):
        actual = add_defense({'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou stubmle across an antique shop and leave with a " \
                          "styrofoam shield, all attacks are now reduced by 2\n"
        self.assertEqual(actual, {'defence': 2})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_add_max_defence(self, mock_print, _):
        actual = add_defense({'defence': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nYou stubmle across an antique shop and leave with a " \
                          "kevelar vest, all attacks are now reduced by 4\n"
        self.assertEqual(actual, {'defence': 4})
        self.assertEqual(expected_output, the_game_printed_this)
