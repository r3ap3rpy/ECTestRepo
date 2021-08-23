import multiprocessing

def sum(a,b):
    result = a + b
    print(f"The result is: {result}")
    return result

def cube(x):
    result = x ** 3
    print(f"The result is: {result}")
    return result

if __name__ == '__main__':
    p = multiprocessing.Process(target=sum, args=(10,15))
    p.start()
    p.join()
    p = multiprocessing.Process(target=cube, args=(10,))
    p.start()
    p.join()