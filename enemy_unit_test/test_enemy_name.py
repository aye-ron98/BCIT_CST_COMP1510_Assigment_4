from unittest import TestCase
from unittest.mock import patch
from enemy import enemy_name


class TestEnemyName(TestCase):

    @patch('random.randint', return_value=3)
    def test_enemy_name(self, _):
        actual = enemy_name()
        self.assertEqual('rue paul', actual)

    @patch('random.randint', return_value=1)
    def test_enemy_name_boundry_start(self, _):
        actual = enemy_name()
        self.assertEqual('bob', actual)

    @patch('random.randint', return_value=7)
    def test_enemy_boundry_end(self, _):
        actual = enemy_name()
        self.assertEqual('uncle sam', actual)
