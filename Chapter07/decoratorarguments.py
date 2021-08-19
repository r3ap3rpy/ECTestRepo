def dec_with_args(function):
    def wrapper_with_args(a, b):
        print(f"Argument a is {a} and argument b is {b}")
        return function(a, b)
    return wrapper_with_args

@dec_with_args
def cities(first, second):
    return f"My most favourite cities are {first} and {second}!"

print(cities('Punta Umbria','Helsinki'))