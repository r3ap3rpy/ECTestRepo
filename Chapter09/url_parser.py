import requests
from threading import Thread, current_thread
from queue import Queue
from time import sleep, time

urls = [
    'http://google.com',
    'https://hu-hu.facebook.com',
    'http://haon.hu',
    'https://arstechnica.com/'
]
for i in range(3):
    urls.extend(urls)

print(f"A total number of {len(urls)} url(s) will be inspected!")

jobQueue = Queue()
resultQueue = Queue()

class URLParser(Thread):
    def __init__(self, jobqueue, resultqueue):
        Thread.__init__(self)
        self.jobqueue = jobqueue
        self.resultqueue = resultqueue

    def run(self):
        while True:
            current_url = self.jobqueue.get()
            #print(f"The thread: {current_thread()} started working on the url: {current_url}")
            urlResult = "N.A."
            try:
                urlResult = requests.get(url = current_url).status_code
            except Exception as e:
                urlResult = str(e)
            #print(f"The current thread: {crrent_thread()} recieved a status code: {urlResult} for the url: {current_url}")
            self.resultqueue.put([current_url, urlResult])
            self.resultqueue.task_done()
            self.jobqueue.task_done()

def QueueWatcher(jobq):
    jobq = jobq
    Total = jobq.qsize()
    while not jobq.empty():
        sleep(0.5)
        print(f"There are {jobq.qsize()} of {Total} elements remaining!",end='\r')

start = time()

for url in urls:
    jobQueue.put(url)

jq = Thread(target=QueueWatcher, args=(jobQueue,))
jq.start()

print("Kicking off the threads!")
for i in range(10):
    t = URLParser(jobQueue, resultQueue)
    t.setDaemon(True)
    t.start()

print("Waiting for the threads to complete!")
jobQueue.join()
stop = time()
#round(float,number_of_digits)
print(f"This whole execution took: {round((stop-start),2)} seconds!")
