
from unittest import TestCase

import world_building
from world_building import describe_current_location
from unittest.mock import patch
import io


class TestDesribeCurrentLocation(TestCase):

    @patch('builtins.range', return_value=(0, 0))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_print, __):
        describe_current_location({'location': (0, 1)})
        expected = '(!)  (!)  (!)  (!)'
        actual = mock_print.getvalue()
        self.assertEqual(expected, actual)


