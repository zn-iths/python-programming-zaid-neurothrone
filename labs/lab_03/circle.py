from math import pi

from position import Position
from shape import Shape
from validation import validate_input
from validation import validate_scalars


class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        validate_input(self.__class__.__name__, [x, y, radius])
        validate_scalars(self.__class__.__name__, [radius])
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
        # TODO: implement with the help of radius
        pass

    @staticmethod
    def is_radius_valid(radius: float) -> bool:
        return radius > 0
