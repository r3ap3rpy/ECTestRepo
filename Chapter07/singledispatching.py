from functools import singledispatch

@singledispatch
def fun(arg, verbose = False):
    if verbose:
        print("Additionaly I would like to say", end = '')
    print(arg)

@fun.register
def _(arg: int, verbose = False):
    if verbose:
        print("The strength is in numbers!", end = '')
    print(arg)

@fun.register
def _(arg: list, verbose = False):
    if verbose:
        print("Let's enumerate!")
        for i, item in enumerate(arg):
            print(f"i = {i}, item = {item}")

fun('This is a string!',verbose=True)
fun(1,verbose=True)
fun({'a':1,'b':2,'c':3}, verbose = True)