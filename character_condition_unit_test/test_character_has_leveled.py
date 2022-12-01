from unittest import TestCase
from character_condition import character_has_leveled


class TestCharacterHasLeveled(TestCase):

    def test_character_has_leveled_level_one_true(self):
        expect = {'damage': 10, 'defence': 10, 'glow up': True, 'hp': 50, 'level': 2, 'xp': 0}
        actual = character_has_leveled({'level': 1, 'xp': 3, 'hp': 10, 'defence': 0, 'damage': 0, 'glow up': False})
        self.assertEqual(expect, actual)

    def test_character_has_leveled_level_one_true_with_damage(self):
        expect = {'damage': 20, 'defence': 10, 'glow up': True, 'hp': 50, 'level': 2, 'xp': 0}
        actual = character_has_leveled({'level': 1, 'xp': 3, 'hp': 10, 'defence': 0, 'damage': 10, 'glow up': False})
        self.assertEqual(expect, actual)

    def test_character_has_leveled_level_one_true_with_defence(self):
        expect = {'damage': 10, 'defence': 20, 'glow up': True, 'hp': 50, 'level': 2, 'xp': 0}
        actual = character_has_leveled({'level': 1, 'xp': 3, 'hp': 10, 'defence': 10, 'damage': 0, 'glow up': False})
        self.assertEqual(expect, actual)

    def test_character_has_leveled_level_one_False(self):
        expect = {'damage': 0, 'defence': 10, 'glow up': False, 'hp': 10, 'level': 1, 'xp': 2}
        actual = character_has_leveled({'level': 1, 'xp': 2, 'hp': 10, 'defence': 10, 'damage': 0, 'glow up': False})
        self.assertEqual(expect, actual)

    def test_character_has_leveled_level_two_False(self):
        expect = {'damage': 0, 'defence': 10, 'glow up': False, 'hp': 10, 'level': 2, 'xp': 2}
        actual = character_has_leveled({'level': 2, 'xp': 2, 'hp': 10, 'defence': 10, 'damage': 0, 'glow up': False})
        self.assertEqual(expect, actual)

    def test_character_has_leveled_level_two_True(self):
        expect = {'damage': 25, 'defence': 35, 'glow up': True, 'hp': 100, 'level': 3, 'level cap': True, 'xp': 0}
        actual = character_has_leveled({'level': 2, 'xp': 5, 'hp': 10, 'defence': 10, 'damage': 0, 'glow up': False})
        self.assertEqual(expect, actual)