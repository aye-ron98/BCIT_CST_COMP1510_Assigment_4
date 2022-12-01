from unittest import TestCase
from character_condition import character_health


class TestCharacterHealth(TestCase):

    def test_character_health(self):
        self.assertEqual(False, character_health({'hp': 1}))

    def test_character_health_zero(self):
        self.assertEqual(True, character_health({'hp': 0}))

    def test_character_health_negative(self):
        self.assertEqual(True, character_health({'hp': -10}))
