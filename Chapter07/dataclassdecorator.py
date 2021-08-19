from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    legs: int
    breed: str
    age: int
    
    def __repr__(self):
        return f"{self.name} has {self.legs}, is of type: {self.breed} is of age: {self.age}"

class Dog:
    def __init__(self, name, legs, breed, age):
        self.name = name
        self.legs = legs
        self.breed = breed
        self.age = age

Suki = Dog(name='Suki',legs = 4, breed='German Shepherd',age=6)
print(Suki)