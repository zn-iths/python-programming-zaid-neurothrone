from math import pow
from math import sqrt


def euclidean_distance(point_a: tuple[int, int],
                       point_b: tuple[int, int]) -> float:
    a_x, a_y = point_a
    b_x, b_y = point_b
    return sqrt(pow((b_x - a_x), 2) + pow((b_y - a_y), 2))


def get_point() -> tuple[int, int]:
    x_coord = int(input("Enter x position: "))
    y_coord = int(input("Enter y position: "))
    return x_coord, y_coord


# a) & b)
print("a) & b)")
print("Get coordinates for Point 1:")
point_1 = get_point()
print("Get coordinates for Point 2:")
point_2 = get_point()
print(f"The euclidean distance between Point 1 [{point_1}] and "
      f"Point 2 [{point_2}] is [{euclidean_distance(point_1, point_2):.2f}].")


print("\nc)")
ORIGO = (0, 0)
POINTS = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]

for point in POINTS:
    print(f"Euclidean distance: [{euclidean_distance(ORIGO, point):.2f}]")
