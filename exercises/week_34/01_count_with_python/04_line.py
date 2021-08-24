def straight_linear_equation(a_coords: tuple[int, int],
                             b_coords: tuple[int, int]) -> None:
    a_x, a_y = a_coords
    b_x, b_y = b_coords

    k = (b_y - a_y) / (b_x - a_x)

    # formula for straight line equation
    # y = k * x + m => m = y - (k * x)
    m = int(a_y - (k * a_x))

    print(f"k = {k}")
    print(f"m = {m}")

    print("y = kx + m")
    print(f"y = {k}x + {m}")


straight_linear_equation(a_coords=(4, 4), b_coords=(0, 1))
