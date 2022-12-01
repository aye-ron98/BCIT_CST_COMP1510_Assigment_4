from unittest import TestCase
from battle_mechanics import remove_ultimate


class TestRemoveUltimate(TestCase):

    def test_remove_ultimate_no_ultimate(self):
        self.assertEqual(('kick', 10), remove_ultimate(('kick', 10)))

    def test_remove_ultimate(self):
        self.assertEqual(('penultimate', 10), remove_ultimate(('ultimate', 10)))
