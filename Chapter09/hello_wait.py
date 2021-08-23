from threading import Thread
from time import sleep

def wait_function(seconds):
    print(f"We are waiting for: {seconds} second(s), to give back the control!")
    sleep(seconds)

wait_thread = Thread(target=wait_function, args=(10,))
print("The thread was kicked off!")
wait_thread.start()
wait_thread.join() 
print("The thread has completed!")