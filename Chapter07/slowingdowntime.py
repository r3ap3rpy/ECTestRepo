from functools import wraps
from time import sleep
import time
import requests

def slow_down_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(0.1)
        value = func(*args, **kwargs) 
        return value
    return wrapper

@slow_down_time
def google_query(number_of_times):    
    for i in range(number_of_times):
        start_time = time.perf_counter()
        print(requests.get('https://google.com').status_code)
        end_time = time.perf_counter()        
        run_time = end_time - start_time
        print(f"We finished the function: {google_query.__name__!r} in {run_time:.4f} seconds!")
        

if __name__ == '__main__':
    google_query(100)