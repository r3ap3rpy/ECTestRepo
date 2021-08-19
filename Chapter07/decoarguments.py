def decorator_with_arguments(arg1, arg2, arg3):
    """
    This is a decorator taking arugment!
    """
    def decorator(func):
        def wrapper(farg1, farg2, farg3):
            print("Coming from wrapper!")
            print(f"arg1 is {arg1}")
            print(f"arg2 is {arg2}")
            print(f"arg3 is {arg3}")
            print(f"farg1 is {farg1}")
            print(f"farg2 is {farg2}")
            print(f"farg3 is {farg3}")
            return func(farg1, farg2, farg3)
        return wrapper
    return decorator
@decorator_with_arguments("New York","London","Paris")
def deco_with_arguments(farg1, farg2, farg3):
    print(f"This is the decorated function farg1 is {farg1}")
    print(f"This is the decorated function farg2 is {farg2}")
    print(f"This is the decorated function farg3 is {farg3}")

print(deco_with_arguments("First","Second","Third"))

print(decorator_with_arguments.__doc__)