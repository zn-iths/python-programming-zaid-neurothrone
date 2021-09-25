from abc import ABC
from abc import abstractmethod

from position import Position
from validation import Validator


class Shape(ABC):
    """The Shape object has a position, circumference and an area.

    The Shape abstract class represents a generic geometric shape
    and common attributes and methods that it should implement.

    Args:
        x (float): the position on the x axis.
        y (float): the position on the y axis.

    Attributes:
        position (Position): the (x, y) Cartesian coordinates.
    """

    def __init__(self, x: float, y: float) -> None:
        self.position = Position(x, y)

    def __eq__(self, other: "Shape") -> bool:
        """Returns whether the type of this object is equal to the type of the other object.

        Returns:
            bool: True if equal, False otherwise
        """

        return type(self) == type(other)

    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} object in the position {self.position}"

    @Validator.args_type(expected_types=(float, int), exclude=True, indices=[0])
    def translate(self, distance_x: float, distance_y: float) -> None:
        """Translates the object horizontally and vertically.

        Args:
            distance_x (float): the amount of translation on the x axis.
            distance_y (float): the amount of translation on the y axis.
        """

        self.position.x += distance_x
        self.position.y += distance_y

    @abstractmethod
    def area(self) -> float:
        """Returns the area of the Shape object.

        Returns:
            float: the area of the Shape object.
        """
        pass

    @abstractmethod
    def circumference(self) -> float:
        """Returns the circumference of the Shape object.

        Returns:
            float: the circumference of the Shape Object.
        """
        pass

    @abstractmethod
    def is_inside(self, position: Position) -> bool:
        """Returns whether the Position is inside the Shape object's circumference.

        Args:
            position (Position): a position object with x, y coordinates.

        Returns:
            bool: True if position is inside the circumference or False otherwise
        """
        pass
