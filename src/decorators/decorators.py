import time
import functools
from logging import log, INFO

def timed(func) -> None:
    """
    Decorator to measure functions execution
    :param func: The function to measure
    :return: None
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, *kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        message = f"{func.__name__} took {elapsed_time} seconds to execute"
        log(INFO, message)
        return result
    return wrapper()