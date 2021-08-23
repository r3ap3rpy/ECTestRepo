import multiprocessing
import logging

def worker():
    print("Just minding our own business!")
    logging.critical("This is baaad!")

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker, args=())
    p.start()
    p.join()