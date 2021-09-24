from position import Position
from shape import Shape
from validation import validate_input
from validation import validate_scalars


class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, length: float) -> None:
        validate_input(self.__class__.__name__, [x, y, width, length])
        validate_scalars(self.__class__.__name__, [width, length])
        super().__init__(x, y)
        self.width = width
        self.length = length

    def __eq__(self, other: "Rectangle") -> bool:
        return all([super().__eq__(other),
                    self.width == other.width,
                    self.length == other.length])

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.position.x}, y={self.position.y}" \
               f", width={self.width}, length={self.length})"

    def __str__(self):
        return super().__str__() + f" with a width of {self.width} and length of {self.length}"

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value) -> None:
        self._length = value

    def area(self) -> float:
        return self.width * self.length

    def circumference(self) -> float:
        return self.width * 2 + self.length * 2

    def is_inside(self, position: Position) -> bool:
        # TODO: implement by width and length
        min_x = self.position.x - self.width / 2
        max_x = self.position.x + self.width / 2
        min_y = self.position.y - self.length / 2
        max_y = self.position.y + self.length / 2
        return min_x <= position.x <= max_x and min_y <= position.x <= max_y
