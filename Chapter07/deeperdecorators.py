# func1, func2
def my_decorator(func_arg):
    def wrapper():
        print("This decorator is printing numbers!")
        for i in range(5):
            print(i * i)
        print("The decorator is done, Control is back at the original function!")
        print(func_arg())
    return wrapper

@my_decorator
def new_function():
    text = "I am the original function!"
    return text

if __name__ == '__main__':
    new_function()