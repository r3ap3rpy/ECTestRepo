from multiprocessing import Process, Value, Array

def function(n, a):
    n.value = 3.14
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i',range(5))

    p = Process(target=function, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])