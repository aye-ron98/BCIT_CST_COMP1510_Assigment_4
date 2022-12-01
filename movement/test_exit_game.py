from unittest import TestCase
from movment import exit_game


class TestExitGame(TestCase):

    def test_exit_game(self):
        expected = {'exit': True}
        actual = exit_game('5', {'exit': False})
        self.assertEqual(expected, actual)

    def test_exit_game_False(self):
        expected = {'exit': False}
        actual = exit_game('0', {'exit': False})
        self.assertEqual(expected, actual)
