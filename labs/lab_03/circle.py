from math import pi

from position import Position
from shape import Shape
from validation import Validator

from shared.mathematics.distance import euclidean_distance


class Circle(Shape):
    """The Circle object has a position, radius, circumference and an area.

    The Circle object represents a circular shape with a
    position of (x, y) in the Cartesian coordinate system and
    has a radius.

    Args:
        x (float): the position on the x axis.
        y (float): the position on the y axis.
        radius (float): a scalar quantity of a radius.

    Attributes:
        position (Position): the (x, y) Cartesian coordinates.
        radius (float): the radius of the circle.
    """

    @Validator.init_args_negative(exclude=True, indices=[0, 1])
    @Validator.init_args_type(exclude=False)
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other: "Circle") -> bool:
        return super().__eq__(other) and self.radius == other.radius

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.position.x}, y={self.position.y}" \
               f", radius={self.radius})"

    def __str__(self):
        return super().__str__() + f" with a radius of {self.radius}"

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value) -> None:
        self._radius = value

    def area(self) -> float:
        return pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * pi * self.radius

    def is_inside(self, position: Position) -> bool:
        distance = euclidean_distance(position.values, self.position.values)
        return distance < self.radius

    @staticmethod
    def is_radius_valid(radius: float) -> bool:
        """Returns whether the radius is greater than zero.

        Args:
            radius (float): a scalar quantity of radius.

        Returns:
            bool: True if radius is greater than zero, False otherwise.
        """

        return radius > 0
