def validate_input(obj_name: str, values: list[float]) -> None:
    for value in values:
        if not isinstance(value, (float, int)):
            raise TypeError(f"{obj_name} object was provided invalid input."
                            f" Only float and int is supported.")


def validate_scalars(obj_name: str, scalars: list[float]) -> None:
    for scalar in scalars:
        if scalar <= 0:
            raise ValueError(f"{obj_name} object was provided a negative or zero value.")
