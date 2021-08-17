import cProfile
from time import sleep

def foo():
    for i in range(10):
        sleep(1)
        print(i)

if __name__ == '__main__':
    print(cProfile.run('foo()'))
