from unittest import TestCase
from enemy import make_final_boss
from unittest.mock import patch


class TestMakeFinalBoss(TestCase):

    @patch('enemy.enemy_name', return_value='Rob')
    def test_make_final_boss(self, mock_name):
        self.assertEqual({'name': 'Rob', 'moves': [], 'hp': 50, 'damage': 15, 'defence': 10}, make_final_boss())
