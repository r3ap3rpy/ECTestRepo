import concurrent.futures
import logging 
import time

def log_function(name):
    logging.info(f"Thread {name} is starting!")
    time.sleep(3)
    logging.info(f"Thread {name} is finishing!")

format = "%(asctime)s: %(message)s"
logging.basicConfig(filename='ThreadPoolExecutor.logs',format=format, level=logging.INFO, datefmt="%H:%M:%S")

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(log_function, range(10))

for i in range(10):
    log_function(i)