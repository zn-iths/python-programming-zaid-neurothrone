from functools import wraps
from typing import Callable


# TODO: attempt to refactor code (repeated three times)

class Validator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def init_args_type(exclude: bool = False, indices: list[int] = None):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                args_ = kwargs.values()
                if exclude:
                    args_ = [arg for index, arg in enumerate(args_) if index not in indices]
                for value in args_:
                    if not isinstance(value, (float, int)):
                        raise TypeError(f"Invalid input. Only float and int is supported.")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def init_args_negative(exclude: bool = False, indices: list[int] = None):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                args_ = kwargs.values()
                if exclude:
                    args_ = [arg for index, arg in enumerate(args_) if index not in indices]
                for value in args_:
                    if value < 0:
                        raise ValueError(f"Value is negative.")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def args_type(exclude: bool = False, indices: list[int] = None):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                args_ = args
                if exclude:
                    args_ = [arg for index, arg in enumerate(args) if index not in indices]
                for value in args_:
                    if not isinstance(value, (float, int)):
                        raise TypeError(f"Invalid input. Only float and int is supported.")
                return func(*args, **kwargs)
            return wrapper
        return decorator
