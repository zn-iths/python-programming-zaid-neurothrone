import unittest

from shared.week_38_oop.field import Field
from shared.week_38_oop.field import Clay
from shared.week_38_oop.field import Crop
from shared.week_38_oop.field import Iron
from shared.week_38_oop.field import Lumber
from shared.week_38_oop.village import Village
from shared.week_38_oop.warehouse import Warehouse


class TestSimpleTravian(unittest.TestCase):
    def test_subclasses_repr(self):
        clay = Clay()
        self.assertEqual(clay.__repr__(), "Clay(0)")
        self.assertNotEqual(clay.__repr__(), "Field(0)")

        crop = Crop()
        self.assertEqual(crop.__repr__(), "Crop(0)")
        self.assertNotEqual(crop.__repr__(), "Field(0)")

        iron = Iron()
        self.assertEqual(iron.__repr__(), "Iron(0)")
        self.assertNotEqual(iron.__repr__(), "Field(0)")

        lumber = Lumber()
        self.assertEqual(lumber.__repr__(), "Lumber(0)")
        self.assertNotEqual(lumber.__repr__(), "Field(0)")

    def test_warehouse_exceed_stock(self):
        Field.PRODUCTION_RATE = 500
        Warehouse.MAX_CAPACITY = 1500
        village = Village()
        for _ in range(4):
            village.skip_hour()
            village.warehouse.update_stock()

        for amount in village.warehouse.stock.values():
            self.assertEqual(village.warehouse.MAX_CAPACITY, amount)

    def test_village_creation(self):
        fields_amount = 15
        fields = [Crop() for _ in range(fields_amount)]
        village = Village(*fields)
        self.assertEqual(len(village.warehouse.fields), fields_amount)


if __name__ == "__main__":
    unittest.main()
