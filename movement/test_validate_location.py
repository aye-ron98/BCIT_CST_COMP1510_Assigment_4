from unittest import TestCase
from movment import validate_location


class TestValidateLocation(TestCase):

    def test_validate_location(self):
        expect = (3, 3)
        actual = validate_location(1, [('move south', (0, -1)), ('move north', (1, 0))], {'location': (3, 4)})
        self.assertEqual(expect, actual)

    def test_validate_location_negative_values(self):
        expect = (-3, -3)
        actual = validate_location(1, [('move south', (-1, -1))], {'location': (-2, -2)})
        self.assertEqual(expect, actual)

    def test_validate_location_zero(self):
        expect = (0, 0)
        actual = validate_location(1, [('move south', (-1, -1))], {'location': (1, 1)})
        self.assertEqual(expect, actual)

    def test_validate_location_X_zero(self):
        expect = (0, 2)
        actual = validate_location(1, [('move south', (-1, 1))], {'location': (1, 1)})
        self.assertEqual(expect, actual)

    def test_validate_location_Y_zero(self):
        expect = (2, 0)
        actual = validate_location(1, [('move south', (1, -1))], {'location': (1, 1)})
        self.assertEqual(expect, actual)

    def test_validate_location_X_negative(self):
        expect = (-1, 2)
        actual = validate_location(1, [('move south', (-1, 1))], {'location': (0, 1)})
        self.assertEqual(expect, actual)

    def test_validate_location_Y_negative(self):
        expect = (2, -1)
        actual = validate_location(1, [('move south', (1, -1))], {'location': (1, 0)})
        self.assertEqual(expect, actual)
