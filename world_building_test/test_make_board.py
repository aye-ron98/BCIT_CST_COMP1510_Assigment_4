from unittest import TestCase
from world_building import make_board


class TestMakeBoard(TestCase):

    def test_make_board(self):
        actual = make_board(5, 5)
        self.assertEqual(25, len(actual.keys()))

    def test_make_board_1_by_1(self):
        actual = make_board(1, 1)
        self.assertEqual(1, len(actual.keys()))
