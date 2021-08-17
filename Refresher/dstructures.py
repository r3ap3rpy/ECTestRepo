a = 1
b = 'This is a string'
c = 1.1
#set
#tuple
#list O(n-1)
#dictionary O(1)

def hello_world(*args, **kwargs):
    for arg in args:
        print(f":: {arg} ::")
    print(kwargs)
    print("Message")
    return args

return_value = hello_world('first','second',a=10,b=20)
print(return_value)

def hello(a, b, c=10, d = 20):
    print(a,b)
    print(c,d)

hello(1,2,c=99, d = 50)
