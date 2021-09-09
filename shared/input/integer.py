import sys

MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize - 1


def get_int_input(message: str = "",
                  min_: int = MIN_INT,
                  max_: int = MAX_INT) -> int:
    while True:
        try:
            user_input = int(input(message))
            if min_ <= user_input <= max_:
                return user_input
            print(f"[Error]: Input can not be less than {min_} or greater than {max_}.")
        except ValueError:
            print(f"[Error]: That is not an integer.")
