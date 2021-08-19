from collections import namedtuple
from dataclasses import dataclass
# typename, field_name, *

Student = namedtuple('Student',['name','age','gpa'])

#class Student(object):
#    def __init__(self, name, age, gpa):
#        self.name = name
#        self.age = age
#        self.gpa = gpa
#    def __repr__(self):
#        return f"Student(name='{self.name}', age='{self.age}', gpa='{self.gpa}'))"

#@dataclass
#class Student(object):
#    name: str
#    age: int
#    gpa: float
#    def __repr__(self):
#        return f"Student(name='{self.name}', age='{self.age}', gpa='{self.gpa}'))"
Daniel = Student('Daniel',30,4)
Jack = Student('Jack',20,4)

print(Daniel)
print(Jack)

print(f"Name: {Daniel.name}, age: {Daniel.age}, GPA: {Daniel.gpa}")
print(f"Name: {Jack.name}, age: {Jack.age}, GPA: {Jack.gpa}")