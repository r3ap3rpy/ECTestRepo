from collections import UserDict

class MyDictionary(UserDict):
    def __del__(self):
        raise RuntimeError("Deletion is forbidden!")
    def pop(self, s = None):
        raise RuntimeError("Removing items is forbidden!")
    def popitem(self, s = None):
        raise RuntimeError("Removing items if forbidden!")

a = MyDictionary({'a':1,'b':2,'c':3})
a.pop()