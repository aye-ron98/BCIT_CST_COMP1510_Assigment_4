from unittest import TestCase
from unittest.mock import patch
import io
from scenarios import riddle


class TestRiddle(TestCase):

    @patch('builtins.input', side_effect='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_riddle_input_correct(self, mock_print, _):
        actual = riddle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:" \
                          "\n What month of the year has 28 days?" \
                          "\n1 :  all of them\n2 :  february\n3 :  december\n4 :  what's a month?" \
                          "\nCorrect! You gain 1xp, you are now at 1\n"
        self.assertEqual({'xp': 1}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_riddle_input_incorrect(self, mock_print, _):
        actual = riddle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:" \
                          "\n What month of the year has 28 days?" \
                          "\n1 :  all of them\n2 :  february\n3 :  december\n4 :  what's a month?" \
                          "\nThe right answer was a all of them! You lave with nothing\n"
        self.assertEqual(None, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_riddle_input_incorrect_max_choice(self, mock_print, _):
        actual = riddle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:" \
                          "\n What month of the year has 28 days?" \
                          "\n1 :  all of them\n2 :  february\n3 :  december\n4 :  what's a month?" \
                          "\nThe right answer was a all of them! You lave with nothing\n"
        self.assertEqual(None, actual)
        self.assertEqual(expected_output, the_game_printed_this)
