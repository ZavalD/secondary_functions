from functools import wraps
from time import time


def execution_time(func):
    @wraps(func)
    def wrap(*args, **kw):
        start_time = time()
        result = func(*args, **kw)
        end_time = time()
        delta_time = end_time - start_time
        # TODO: ADD logger
        text = f'Function {func.__name__} took {delta_time} seconds to execute'
        print(text)
        return result
    return wrap
