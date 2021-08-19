def uppercase(function):
    def wrapper():
        return function().upper()
    return wrapper

@uppercase
def say_something():
    return f"Welcome to the decorators!"

print(say_something())