import threading

l = threading.Lock()
print(f"Before acquire!")
l.acquire()
print(f"After first acquire and before second!")
l.acquire()
print(f"Acquired lock twice!")