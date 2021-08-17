"""
__init__
__new__
cls
self
@classmethod
@staticmethod
__str__
__repr__
"""

class Singleton(object):
    def __init__(self):
        self.a = 88
        self.__hidden = -1
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance
    
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, value):
        self.__hidden = value

    @classmethod
    def class_method(cls):
        return "I am a callable classmethod of Singleton!"
    
    @staticmethod 
    def static_method(a = 99):
        return "I am a static method of Singleton!"
    
    def __str__(self):
        return f"I am  the override of __str__ : {self.__class__.__name__}"
    def __repr__(self):
        return f"I am the override of __repr__ : {self.__class__.__name__}"  

a = Singleton()
b = Singleton()
c = Singleton()
print(a)
print(repr(b))
print(id(a))
print(id(b))
print(a.a)
a.a = 99
print(b.a)
print(a._Singleton__hidden)
print(dir(a))
print(a.hidden)
a.hidden = 100
print(c.hidden)

    