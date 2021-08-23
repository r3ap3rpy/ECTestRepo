import multiprocessing
import random
from time import sleep
class Worker(multiprocessing.Process):
    def run(self):
        waitfor =  random.randint(0,5)
        print(f"Waiting for {waitfor} second(s)!")
        sleep(waitfor)

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = Worker()
        jobs.append(p)
        p.start()
    
    for j in jobs:
        j.join()