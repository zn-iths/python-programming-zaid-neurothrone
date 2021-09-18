import sys

MAX_FLOAT = sys.float_info.max
MIN_FLOAT = sys.float_info.min


def get_float_input(message: str = "",
                    min_: float = MIN_FLOAT,
                    max_: float = MAX_FLOAT) -> float:
    while True:
        try:
            user_input = float(input(message))
            if min_ <= user_input <= max_:
                return user_input
            print(f"[Error]: Input can not be less than {min_} or greater than {max_}.")
        except ValueError:
            print(f"[Error]: That is not a number.")
