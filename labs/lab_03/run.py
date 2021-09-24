from circle import Circle
from rectangle import Rectangle
from position import Position


def main():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(1, 1, 1)
    rectangle = Rectangle(0, 0, 1, 1)

    print(circle1 == circle2)
    print(circle2 == rectangle)

    print(circle1.is_inside(Position(0.5, 0.5)))
    circle1.translate(5, 5)
    print(circle1.is_inside(Position(0.5, 0.5)))
    circle1.translate("Three", 5)

    # circle3 = Circle(2, 1, "test")
    # print(circle3)
    # rectangle3 = Rectangle("a", 1, 2, 3)
    # print(rectangle3)


if __name__ == "__main__":
    main()
