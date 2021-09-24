class Position:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: "Position") -> bool:
        return self.values == other.values

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        self._y = value

    @property
    def values(self) -> tuple[float, float]:
        return self.x, self.y
