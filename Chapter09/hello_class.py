from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("We are going to wait for 5 seconds!")
        sleep(5)

#active_count() -> Return the number of running theads
#current_thread() -> Returns the currently running thread
#enumerate() -> Returns all the running theads!

for i in range(5):
    t = MyThread()
    #t.setDaemon(True)
    t.start()


print("Threads kicked off, waiting for them to complete!")
#sleep(10)
print("The main thread is finished!")

