import unittest

from shared.week_38_oop import Unit


class TestUnit(unittest.TestCase):
    def test_create_unit(self):
        unit = Unit(5)
        self.assertEqual(unit.value, 5)
        self.assertNotEqual(unit.value, "5")
        self.assertIsInstance(unit.value, int)
        self.assertNotIsInstance(unit.value, str)

    def test_invalid_value_arg(self):
        unit = Unit(5)
        with self.assertRaises(ValueError):
            unit.value = None
            unit.value = -5

    def test_inches_to_cm(self):
        unit = Unit(5)
        self.assertEqual(unit.inches_to_cm(), 12.7)
        self.assertNotEqual(unit.inches_to_cm(), 2.54)
        self.assertNotEqual(unit.inches_to_cm(), "abcd")
        self.assertGreater(unit.value, -1)
        self.assertIsNotNone(unit.value)

    def test_foot_to_meters(self):
        unit = Unit(5)
        self.assertEqual(unit.foot_to_meters(), 1.524)
        self.assertNotEqual(unit.foot_to_meters(), 1.5)

    def test_pound_to_kg(self):
        unit = Unit(5)
        self.assertEqual(unit.pound_to_kg(), 2.26796)
        self.assertNotEqual(unit.pound_to_kg(), 2.3)

    def test_repr(self):
        unit = Unit(5)
        self.assertEqual(unit.__repr__(), "Unit(5)")
        self.assertNotEqual(unit.__repr__(), "Unit(5")


if __name__ == "__main__":
    unittest.main()
