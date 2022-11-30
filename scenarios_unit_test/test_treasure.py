from unittest import TestCase
from unittest.mock import patch
from scenarios import treasure
import io


class TestTreasure(TestCase):

    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_min(self, mock_print, mock_number):
        actual = treasure({'damage': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nIt's your luck day!, You stumble across an armory, you leave with a stick. " \
                          "ALl damage is now increased by +3.\n"
        self.assertEqual(actual, {'damage': 3})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure(self, mock_print, mock_number):
        actual = treasure({'damage': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nIt's your luck day!, You stumble across an armory, you leave with a battering ram. " \
                          "ALl damage is now increased by +5.\n"
        self.assertEqual(actual, {'damage': 5})
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_min(self, mock_print, mock_number):
        actual = treasure({'damage': 0})
        the_game_printed_this = mock_print.getvalue()
        expected_output = "\nIt's your luck day!, You stumble across an armory, you leave with a flag pole. " \
                          "ALl damage is now increased by +7.\n"
        self.assertEqual(actual, {'damage': 7})
        self.assertEqual(expected_output, the_game_printed_this)




