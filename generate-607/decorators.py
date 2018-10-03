import functools
import time


def timer(func):
    """Print the runtime of the decoreted function

    Arguments:
        func {[object]} -- The function to be decorated
    """
    @functools.wraps(func)
    def wrapper_timer(*arg, **kwargs):
        start_time = time.perf_counter()
        value = func(*arg, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function {func.__name__!r}: Time elapsed {run_time:.4f} secs")
        return value
    return wrapper_timer
