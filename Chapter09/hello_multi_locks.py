import multiprocessing

def update_db(lock, data):
    lock.acquire()
    try:
        print(f"We are updating critical data: {data}")
    finally:
        lock.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(5):
        multiprocessing.Process(target=update_db, args=(lock, "DELETE FROM DATABASE")).start()

