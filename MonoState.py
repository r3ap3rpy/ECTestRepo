class Monostate(object):
    __internal_state = {'A':5,'B':6}
    def __init__(self):
        self.__dict__ = self.__internal_state

class Monostatev2(object):
    _internal_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostatev2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._internal_state
        return obj

A = Monostate()
B = Monostate()

A.x = 10
print(B.x)
B.x = 99
print(A.x)

A = Monostatev2()
B = Monostatev2()

A.y = 100
print(B.y)
