from math import pi
from typing import Union
import unittest

from circle import Circle
from rectangle import Rectangle
from position import Position
from shape import Shape


class TestShapeClasses(unittest.TestCase):
    def test_base_cases(self):
        """Test base cases of requirement specification."""

        c1 = Circle(x=0, y=0, radius=1)
        c2 = Circle(x=1, y=1, radius=1)
        r1 = Rectangle(x=0, y=0, width=1, length=1)
        self.assertEqual(c1, c2)
        self.assertNotEqual(c2, r1)
        self.assertTrue(c1.is_inside(Position(0.5, 0.5)))
        c1.translate(5, 5)
        self.assertFalse(c1.is_inside(Position(0.5, 0.5)))

    def test_validation(self):
        """Validation tests when passing negative or zero values and strings."""

        with self.assertRaises(ValueError):
            c1 = Circle(x=0, y=0, radius=0)
            c2 = Circle(x=0, y=0, radius=-5)
            r1 = Rectangle(x=0, y=0, width=-2, length=2)
        with self.assertRaises(TypeError):
            c3 = Circle(x=0, y=0, radius=2)
            c3.translate("Three", 5)
            r2 = Rectangle(x=0, y=0, width=2, length="one")
            # instantiation of an abstract class should raise a TypeError
            shape = Shape(5, 5)

    def test_translation(self):
        """Test subclasses translation method."""

        c1 = Circle(x=0, y=0, radius=2)
        start = c1.position.values
        c1.translate(2, 2)
        end = c1.position.values
        self.assertNotEqual(start, end)
        self.assertEqual((2, 2), end)
        r1 = Rectangle(x=2, y=2, width=1, length=1)
        rect_start = r1.position.values
        r1.translate(-4, -4)
        rect_end = r1.position.values
        self.assertNotEqual(rect_start, rect_end)
        self.assertEqual(rect_end, (-2, -2))

    def test_math_computations(self):
        """Test computations of subclasses circumference and area methods."""

        r1 = Rectangle(x=0, y=0, width=2, length=2)
        c1 = Circle(x=0, y=0, radius=2)
        self.assertEqual(2 * 2, r1.area())
        self.assertEqual(2 * r1.width + 2 * r1.length, r1.circumference())
        self.assertEqual(pi * c1.radius ** 2, c1.area())
        self.assertEqual(pi * 2 * c1.radius, c1.circumference())

    def test_polymorphism(self):
        """Test polymorphism of Shape subclasses without raising an exception."""

        # tests that should fail
        for value in ("woop", -5):
            with self.assertRaises((TypeError, ValueError)):
                self.polymorphism_test_variance(test_variable=value)

        # test that should succeed
        try:
            self.polymorphism_test_variance(5)
        except (TypeError, ValueError):
            self.fail(f"{self.test_polymorphism().__name__} test failed.")

    @staticmethod
    def polymorphism_test_variance(test_variable: Union[float, int, str]) -> None:
        shapes = [
            Circle(x=0, y=0, radius=test_variable),
            Circle(x=1, y=1, radius=1),
            Rectangle(x=0, y=0, width=1, length=1),
            Rectangle(x=0, y=0, width=2, length=2)
        ]

        for shape in shapes:
            print(shape.area())
            print(shape.circumference())


def main():
    unittest.main()


if __name__ == "__main__":
    main()
