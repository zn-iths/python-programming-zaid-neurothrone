from abc import ABC
from abc import abstractmethod

from position import Position


# TODO: docstrings


class Shape(ABC):
    def __init__(self, x: float, y: float) -> None:
        self.position = Position(x, y)

    def __eq__(self, other: "Shape") -> bool:
        return type(self) == type(other)

    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} object in the position {self.position}"

    def translate_x(self, distance: float) -> None:
        """Translates the object horizontally."""
        # TODO: ValueError e.g. str
        self.position.x += distance

    def translate_y(self, distance: float) -> None:
        """Translates the object vertically."""
        # TODO: ValueError e.g. str
        self.position.y += distance

    @abstractmethod
    def area(self) -> float:
        """Returns the area of the Shape object."""
        pass

    @abstractmethod
    def circumference(self) -> float:
        """Returns the circumference of the Shape object."""
        pass

    @abstractmethod
    def is_inside(self, position: Position) -> bool:
        """Returns if the Position is inside the Shape object's circumference."""
        pass
