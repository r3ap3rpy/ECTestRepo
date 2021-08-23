import logging
import threading
import time

def log_function(name):
    logging.info(f"Thread {name} is starting!")
    time.sleep(3)
    logging.info(f"Thread {name} is finishing!")

format = "%(asctime)s: %(message)s"
logging.basicConfig(filename='Threading.logs',format=format, level=logging.INFO, datefmt="%H:%M:%S")
#logging.info(f"Main thread before spawning children")
#x = threading.Thread(target=log_function, args=(1,))
#logging.info(f"Main thread : Kicking of the children!")
#x.start()
#logging.info(f"Main thread : waiting for the thread to finish!")
#x.join()
#logging.info(f"Main thread : all is done!")
print(F"Whate")
threads = list()
for i in range(10):
    logging.info(f"Main thead is creating thread with index: {(i + 1)}")
    x = threading.Thread(target=log_function, args=((i+1),))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    logging.info(f"Main thead before joinging thread: {(i+1)}")
    thread.join()
    logging.info(f"Main thread has joined thread: {(i+1)}")