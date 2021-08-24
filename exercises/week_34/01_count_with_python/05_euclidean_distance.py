from math import pow
from math import sqrt


def euclidean_distance(point_a: tuple[int, int],
                       point_b: tuple[int, int]) -> None:
    a_x, a_y = point_a
    b_x, b_y = point_b

    # # formula for euclidean distance
    # d = sqrt[(x2 - x1)^2 + (y2 - y1)^2]
    distance = sqrt(
        pow((b_x - a_x), 2) +
        pow((b_y - a_y), 2))

    print(f"distance = {distance:.2f}")


euclidean_distance(point_a=(3, 5), point_b=(-2, 4))
