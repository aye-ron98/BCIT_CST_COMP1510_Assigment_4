from unittest import TestCase
from unittest.mock import patch
import io
from world_building import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=['tommy'])
    def test_make_character(self, _):
        self.assertEqual({'damage': 0, 'defence': 0, 'exit': False, 'glow up': False, 'goal': False, 'hp': 30,
                          'level': 1, 'level cap': False, 'location': (4, 0), 'name': 'tommy', 'xp': 0},
                         make_character())

    @patch('builtins.input', side_effect=['A01280188'])
    def test_make_character_student_number(self, _):
        self.assertEqual({'damage': 0, 'defence': 0, 'exit': False, 'glow up': False, 'goal': False, 'hp': 30,
                          'level': 1, 'level cap': False, 'location': (4, 0), 'name': 'A01280188', 'xp': 0},
                         make_character())

    @patch('builtins.input', side_effect=['', 'tommy'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_character_invalid_name(self, mock_print, mock_input):
        actual = make_character()
        the_game_printed_this = mock_print.getvalue()
        expected_output = 'That is not a name!\n'
        self.assertEqual({'damage': 0, 'defence': 0, 'exit': False, 'glow up': False, 'goal': False, 'hp': 30,
                          'level': 1, 'level cap': False, 'location': (4, 0), 'name': 'tommy', 'xp': 0}, actual)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(expected_output, the_game_printed_this)
