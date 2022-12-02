from unittest import TestCase
from unittest.mock import patch
from scenarios import puzzle
import io


class TestPuzzle(TestCase):

    @patch('builtins.input', side_effect='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_puzzle(self, mock_print, _):
        actual = puzzle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:\n I’m tall when I’m young, and I’m short when I’m old. What am I?" \
                          "\n1 :  a candle\n2 :  a human\n3 :  a tree\n4 :  an eraser" \
                          "\nCorrect! You gain 1xp, you are now at 1\n"
        self.assertEqual({'xp': 1}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_guess_wrong_puzzle_lower_limit(self, mock_print, _):
        actual = puzzle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:\n I’m tall when I’m young, and I’m short when I’m old. What am I?" \
                          "\n1 :  a candle\n2 :  a human\n3 :  a tree\n4 :  an eraser" \
                          "\nThe right answer was a candle! You lave with nothing\n"
        self.assertEqual(None, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_guess_wrong_puzzle_upper_limit(self, mock_print, _):
        actual = puzzle({'xp': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nA stander asks you:\n I’m tall when I’m young, and I’m short when I’m old. What am I?" \
                          "\n1 :  a candle\n2 :  a human\n3 :  a tree\n4 :  an eraser" \
                          "\nThe right answer was a candle! You lave with nothing\n"
        self.assertEqual(None, actual)
        self.assertEqual(expected_output, the_game_printed_this)
