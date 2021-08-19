from collections import UserList

class MyList(UserList):
    def remove(self, s = None):
        raise RuntimeError("Removal is forbidden!")
    def pop(self, s = None):
        raise RuntimeError("Popping is forbidden!")

a = MyList([1,2,3,4,5])
print(a)
a.append(5)
print(a)
a.remove()