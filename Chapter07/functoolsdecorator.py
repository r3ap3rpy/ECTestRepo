from functools import wraps

def upper_case(func):
    @wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@upper_case
def say_hi():
    "This function will say hi!"
    return "Welcome to the functools module!"

print(say_hi())
print(say_hi.__doc__)