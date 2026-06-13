"""Measure user-visible run time so slow functions are easy to spot quickly."""

import time
from functools import wraps


def elapsed_time_profile(func):
    """Wrap a function and print how long the full call took to complete."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Run the original function and emit a readable elapsed-time log."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = end - start
        print(f"[ELAPSED TIME] {func.__name__}: {elapsed:.4f} seconds")

        return result

    return wrapper
