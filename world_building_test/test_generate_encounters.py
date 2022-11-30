from unittest import TestCase
from unittest.mock import patch
from world_building import generate_encounters


class TestGenerateEncounters(TestCase):

    @patch('random.randint', return_value=1)
    def test_generate_encounters_health(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('health', actual)

    @patch('random.randint', return_value=2)
    def test_generate_encounters_damage(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('damage', actual)

    @patch('random.randint', return_value=3)
    def test_generate_encounters_defence(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('defense', actual)

    @patch('random.randint', return_value=4)
    def test_generate_encounters_puzzle(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('puzzle', actual)

    @patch('random.randint', return_value=5)
    def test_generate_encounters_riddle(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('riddle', actual)

    @patch('random.randint', return_value=6)
    def test_generate_encounters_battle(self, mock_number):
        actual = generate_encounters()
        self.assertEqual('battle', actual)


