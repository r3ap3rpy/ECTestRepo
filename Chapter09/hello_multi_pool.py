import multiprocessing

def square(x):
    result = x**2
    print(f"The result is: {result}")
    return result

if __name__ == '__main__':    
    with multiprocessing.Pool(5) as p:
        print(p.map(square,range(10)))