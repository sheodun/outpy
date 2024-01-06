"""The decorators module."""

from functools import wraps


def open_file(open_mode: str):
    """A decorator for opening a file.

    Args:
        open_mode: the open mode of the file, e.g. `w`, `a`, and `r`.
    """

    def open_decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            with open(self.path, open_mode) as f:
                return func(f, *args)

        return wrapper

    return open_decorator
