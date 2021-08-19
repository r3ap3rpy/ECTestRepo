from functools import wraps
import time
from typing_extensions import runtime

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"We finished the function: {func.__name__!r} in {run_time:.4f} seconds!")
        return value
    return wrapper

@timer
def wasting_time(number_of_tasks):
    for _ in range(number_of_tasks):
        sum([i**2 for i in range(10000)])

wasting_time(1000)