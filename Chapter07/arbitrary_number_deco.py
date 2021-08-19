def arbitrary(function):
    #helloWorld(a,b,k=10,j=20)
    def wrapper(*args, **kwargs):
        print(f"Positional arguments: {','.join(args)}")
        print(f"Keyword arguments: {kwargs}")
        function(*args, **kwargs)
    return wrapper

@arbitrary
def demodeco(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print(demodeco('a','b', c=10, d = 20))