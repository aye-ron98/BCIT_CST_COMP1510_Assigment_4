from unittest import TestCase
from unittest.mock import patch

class TestBattleCards(TestCase):


    @patch('random.randint', return_value=2)
    def test_battle_cards(self):
        self.
