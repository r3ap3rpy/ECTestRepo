import threading, time, random,queue

class Producer:
    def __init__(self):
        self.product = ['nail','fork','hammer','cabbage']
        self.next = 0
    
    def run(self):
        global q
        while time.clock() < 10:
            if self.next < time.clock():
                f = self.product[random.randrange(len(self.product))]
                g = self.product[random.randrange(len(self.product))]
                q.put(f)
                q.put(g)
                print(f"We have added: {f} and {g} to the production line!")
                self.next += random.random()

class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        while time.clock() <10:
            print(f"Queue size: {q.qsize()}")
            if self.next < time.clock() and not q.empty():
                f = q.get()
                print(f"Product: {f} was removed from the production line!")
            elif q.empty():
                print(f"Consumer is waiting for product!")

if __name__ == '__main__':
    q = queue.Queue()
    p = Producer()
    c = Consumer()
    pt = threading.Thread(target = p.run, args=())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()
