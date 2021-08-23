import threading

t = threading.Thread(target=print, args=('Hello World'))
t.start()
t.join()