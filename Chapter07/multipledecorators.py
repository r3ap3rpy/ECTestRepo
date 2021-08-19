def uppercase(function):
    def wrapper():
        return function().upper()
    return wrapper

def string_splitter(function):
    def wrapper():
        return function().split()
    return wrapper

@string_splitter
@uppercase
def say_something():
    return "This is what I am talking about!"

print(say_something())
