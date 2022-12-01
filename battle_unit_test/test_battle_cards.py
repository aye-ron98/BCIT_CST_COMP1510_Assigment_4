from unittest import TestCase
from battle_mechanics import battle_cards
from unittest.mock import patch


class TestBattleCards(TestCase):

    @patch('random.randint', return_value=2)
    def test_battle(self, _):
        actual = battle_cards()
        self.assertEqual((('strike', 5), ('stab', 8), ('bite', 2), ('defend', -5), ('guard', -8)), actual)

    @patch('random.randint', return_value=1)
    def test_battle_roll_1(self, _):
        actual = battle_cards()
        self.assertEqual((('strike', 5), ('stab', 8), ('drop kick', 10), ('defend', -5), ('dodge', -10)), actual)

    @patch('random.randint', return_value=9)
    def test_battle_roll_upper_bound_9(self, _):
        actual = battle_cards()
        self.assertEqual((('strike', 5), ('drop kick', 10), ('bite', 2), ('guard', -8), ('garrison', -6)), actual)
