a = 10
b = 20
#**globals()
print(f"a = {a}, b = {b}")

def scoped():
    print("a = {a}, b = {b}".format(a=11,b=22))
#**locals()

def globloc():
    a = 30
    b = 50
    print(f"a = {a}, b = {b}".format(**locals()))
    print(f"a = {a}, b = {b}".format(**globals()))

globloc()

print(f"a = {a}, b = {b}".format(**globals()))