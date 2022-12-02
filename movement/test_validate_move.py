from unittest import TestCase
from movment import validate_move
from unittest.mock import patch
import io


class TestValidateMove(TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_validate_move_lower_bound(self, _):
        self.assertEqual(str(1), validate_move(1, 5))

    @patch('builtins.input', side_effect=[5])
    def test_validate_move_upper_bound(self, _):
        self.assertEqual(str(5), validate_move(1, 5))

    @patch('builtins.input', side_effect=[6, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_out_of_bound_upper(self, mock_print, mock_input):
        actual = validate_move(1, 5)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "That is not an option, try again!\n"
        self.assertEqual(str(1), actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[0, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_out_of_bound_lower(self, mock_print, mock_input):
        actual = validate_move(3, 5)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "That is not an option, try again!\n"
        self.assertEqual(str(3), actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['not an option', 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_string_input(self, mock_print, mock_input):
        actual = validate_move(1, 5)
        the_game_printed_this = mock_print.getvalue()
        expected_output = "That is not an option, try again!\n"
        self.assertEqual(str(2), actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)
