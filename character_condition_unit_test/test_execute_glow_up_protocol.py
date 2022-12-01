from unittest import TestCase
from unittest.mock import patch
from character_condition import execute_glow_up_protocol
import io


class TestExecuteGlowUpProtocol(TestCase):

    @patch('movment.validate_move', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_glow_up_protocol_select_health(self, mock_print, mock_input):
        actual = execute_glow_up_protocol({'name': 'jerry', 'hp': 2, 'glow up': True})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nCongratulations! jerry have leveled up!choose an upgradable from the following!\n" \
                          "\n+10 health :  1\n" \
                          "+10 base damage :  2\n" \
                          "+10 base defence :  3\n" \
                          "\nYour health is now permanently increased by 10, Your total health is now 12\n"
        self.assertEqual({'glow up': False, 'hp': 12, 'name': 'jerry'}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('movment.validate_move', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_glow_up_protocol_select_damage(self, mock_print, mock_input):
        actual = execute_glow_up_protocol({'name': 'jerry', 'damage': 2, 'glow up': True})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nCongratulations! jerry have leveled up!choose an upgradable from the following!\n" \
                          "\n+10 health :  1\n" \
                          "+10 base damage :  2\n" \
                          "+10 base defence :  3\n" \
                          "\nAll attacks now have a +10 attack on top of their normal stats, beware enemy defences, " \
                          "they may still defend against you, your total attack is now 12\n"
        self.assertEqual({'damage': 12, 'glow up': False, 'name': 'jerry'}, actual)
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('movment.validate_move', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_glow_up_protocol_select_damage(self, mock_print, mock_input):
        actual = execute_glow_up_protocol({'name': 'jerry', 'defence': 0, 'glow up': True})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nCongratulations! jerry have leveled up!choose an upgradable from the following!\n" \
                          "\n+10 health :  1\n" \
                          "+10 base damage :  2\n" \
                          "+10 base defence :  3\n" \
                          "\nAll incoming attacks are now reduced by 10!, your total defence is now 10\n"
        self.assertEqual({'defence': 10, 'glow up': False, 'name': 'jerry'}, actual)
        self.assertEqual(expected_output, the_game_printed_this)
