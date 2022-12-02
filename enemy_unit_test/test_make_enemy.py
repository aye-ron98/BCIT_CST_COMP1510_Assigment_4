from unittest import TestCase
from unittest.mock import patch
from enemy import make_enemy


class TestMakeEnemy(TestCase):

    @patch('enemy.enemy_name', return_value='Rue Pual')
    def test_make_enemy(self, _):
        actual = make_enemy({'level': 1, 'hp': 10, 'xp': 1})
        self.assertEqual({'damage': 0, 'defence': 0, 'hp': 4.0, 'name': 'Rue Pual'}, actual)

    @patch('enemy.enemy_name', return_value='Rue Pual')
    @patch('random.randint', return_value=2)
    def test_make_enemy_player_level_2(self, _, __):
        actual = make_enemy({'level': 2, 'hp': 10, 'xp': 1})
        self.assertEqual({'damage': 2, 'defence': 0, 'hp': 35, 'name': 'Rue Pual'}, actual)

    @patch('enemy.enemy_name', return_value='Rue Pual')
    @patch('random.randint', side_effect=[0, 2])
    def test_make_enemy_player_level_2_no_damage(self, _, __):
        actual = make_enemy({'level': 2, 'hp': 10, 'xp': 1})
        self.assertEqual({'damage': 0, 'defence': 2, 'hp': 35, 'name': 'Rue Pual'}, actual)
