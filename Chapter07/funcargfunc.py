def multiplication(x, y):
    return x * y

def div(x, y):
    return x / y

def math(function, x, y):
    return function(x,y)

print(math(multiplication,10,30))
print(math(div, 40,50))

def person(name):
    a = "#####"
    def greeting():
        return f"{a} Welcome"
    return (greeting() + " " + name)

print(person("Jones"))
    