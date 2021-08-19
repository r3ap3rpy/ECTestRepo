class Animal:
    def __init__(self, legs):
        self.__legs = legs

    @property
    def legs(self):
        return self.__legs

    @classmethod
    def do_anything(cls):
        return "I am the class method!"

    @staticmethod
    def do_something(a,b):
        return f"I am the static method! a = {a}, b = {b}"

class Cigarette:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property 
    def total_value(self):
        return f"The cigarette: {self.__name} has a total value of {(self.__price * self.__quantity)} $"

Marlboro = Cigarette(name = 'Marlboro', price = 10, quantity=15)

A = Animal(4)
print(f"This animal has {A.legs} legs!")
print(f"This is the classmethod: {Animal.do_anything()}")
print(f"This is the static method: {A.do_something(10,20)}")

print(Marlboro.total_value)

#def function_name() -> function_name
#this_is_a_function_too = function_name

# Functions can be arugments to other functions!

