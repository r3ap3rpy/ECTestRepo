from numba import jit
import random

@jit(nopython = True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
    if (x ** 2 + y ** 2) < 1.0:
        acc += 1
    return 4.0 * acc / nsamples

if __name__ == '__main__':
    print("First call")
    print(monte_carlo_pi(100))
    print("Second_call")
    print(monte_carlo_pi(100))
    print("End")