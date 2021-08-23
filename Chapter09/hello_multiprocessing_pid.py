import multiprocessing
import os

print(f"The main PID: {os.getpid()}")

def worker1():
    print(f"The ID of worker is: {os.getpid()} with name: {multiprocessing.current_process().name}")

def worker2():
    print(f"The ID of worker is: {os.getpid()} with name: {multiprocessing.current_process().name}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(name="Worker 1",target=worker1,args=())
    p2 = multiprocessing.Process(name="Worker 2",target=worker2,args=())    
    p1.start()
    p2.start()
    print(f"The ID of process 1 is: {p1.pid}")
    print(f"The ID of process 2 is: {p2.pid}")
    p1.join()
    p2.join()
    print(f"Both processes have ran their course!")
    print(f"Is the p1 alive? {p1.is_alive()}")
    print(f"Is the p2 alive? {p2.is_alive()}")