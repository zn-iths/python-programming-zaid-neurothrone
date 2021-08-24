from math import pow
from math import sqrt


def euclidean_distance_3d(point_a: tuple[int, int, int],
                          point_b: tuple[int, int, int]) -> None:
    a_x, a_y, a_z = point_a
    b_x, b_y, b_z = point_b

    # formula for euclidean distance in 3d
    # d = ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)1/2
    distance = sqrt(
        pow((b_x - a_x), 2) +
        pow((b_y - a_y), 2) +
        pow((b_z - a_z), 2))

    print(f"distance = {distance:.2f}")


euclidean_distance_3d(point_a=(2, 1, 4), point_b=(3, 1, 0))
