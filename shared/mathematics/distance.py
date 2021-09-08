from math import sqrt


def euclidean_distance(point_a: tuple[float, float],
                       point_b: tuple[float, float]) -> float:
    a_x, a_y = point_a
    b_x, b_y = point_b
    delta_x = b_x - a_x
    delta_y = b_y - a_y
    return sqrt(delta_x ** 2 + delta_y ** 2)
