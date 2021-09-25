from functools import wraps
from typing import Callable


# TODO: attempt to refactor code (repeated three times)

class Validator:
    """A Validator class with useful validation decorators."""

    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def init_args_type(expected_types: tuple,
                       exclude: bool = False,
                       indices: list[int] = None):
        """Decorator type validator for objects __init__() method.

         Raises a TypeError exception for input that do not match the
         expected types.

        Args:
            expected_types (tuple[type]): the expected data types of the args.
            exclude (bool): whether to exclude one or more args when validating.
            indices (list[int]): the indices to exclude from the args passed in.
        """

        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                args_ = kwargs.values()
                if exclude:
                    args_ = [arg for index, arg in enumerate(args_) if index not in indices]
                for value in args_:
                    if not isinstance(value, expected_types):
                        raise TypeError(f"Invalid input. Only float and int is supported.")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def init_args_negative(exclude: bool = False,
                           indices: list[int] = None):
        """Decorator value validator for objects __init__() method.

         Raises a ValueError exception for numerical values that are negative.

        Args:
            exclude (bool): whether to exclude one or more args when validating.
            indices (list[int]): the indices to exclude from the args passed in.
        """

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
    def args_type(expected_types: tuple,
                  exclude: bool = False,
                  indices: list[int] = None):
        """Decorator type validator for any function method.

         Raises a TypeError exception for input that do not match the
         expected types.

        Args:
            expected_types (tuple[type]): the expected data types of the args.
            exclude (bool): whether to exclude one or more args when validating.
            indices (list[int]): the indices to exclude from the args passed in.
        """

        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                args_ = args
                if exclude:
                    args_ = [arg for index, arg in enumerate(args) if index not in indices]
                for value in args_:
                    if not isinstance(value, expected_types):
                        raise TypeError(f"Invalid input. Only float and int is supported.")
                return func(*args, **kwargs)
            return wrapper
        return decorator
