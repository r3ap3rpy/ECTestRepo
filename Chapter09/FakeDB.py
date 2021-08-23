import threading

class FDB:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def lock_n_update(self, name):
        print("Acquiring Mutex")
        with self.lock:
            # perform the operation
            ...
        print("Releasing lock!")
