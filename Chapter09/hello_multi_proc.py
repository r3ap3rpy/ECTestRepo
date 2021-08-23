import multiprocessing

if __name__ == '__main__':
    p = multiprocessing.Process(target=print, args=('Hello World',))
    p.start()
    p.join()
    