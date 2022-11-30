from unittest import TestCase
from movment import get_user_choice
from unittest.mock import patch
import io


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_quit(self, mock_print, mock_input):
        actual = get_user_choice({'exit': False})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n"
        self.assertEqual({'exit': True}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_north(self, mock_print, mock_input):
        actual = get_user_choice({'location': (4, 0), 'exit': False})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n"
        self.assertEqual({'location': (3, 0), 'exit': False}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_out_of_bounds_upper_limit_x(self, mock_print, mock_input):
        actual = get_user_choice({'location': (4, 0), 'exit': False, 'name': 'tom'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n" \
                          "tom you cannot go that way\n"
        self.assertEqual({'location': (3, 0), 'exit': False, 'name': 'tom'}, actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['1', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_out_of_bounds_lower_limit_x(self, mock_print, mock_input):
        actual = get_user_choice({'location': (0, 0), 'exit': False, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n" \
                          "jerry you cannot go that way\n"
        self.assertEqual({'location': (1, 0), 'exit': False, 'name': 'jerry'}, actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_out_of_bounds_upper_limit_y(self, mock_print, mock_input):
        actual = get_user_choice({'location': (3, 4), 'exit': False, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n" \
                          "jerry you cannot go that way\n"
        self.assertEqual({'location': (4, 4), 'exit': False, 'name': 'jerry'}, actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['4', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_out_of_bounds_lower_limit_y(self, mock_print, mock_input):
        actual = get_user_choice({'location': (3, 0), 'exit': False, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n" \
                          "jerry you cannot go that way\n"
        self.assertEqual({'location': (4, 0), 'exit': False, 'name': 'jerry'}, actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_within_boundry_limit_y(self, mock_print, mock_input):
        actual = get_user_choice({'location': (3, 3), 'exit': False, 'name': 'jerry'})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "1 move north\n" \
                          "2 move east\n" \
                          "3 move south\n" \
                          "4 move west\n" \
                          "5 Quit\n"
        self.assertEqual({'location': (3, 4), 'exit': False, 'name': 'jerry'}, actual)
        self.assertEqual(expected_output, the_game_printed_this)
