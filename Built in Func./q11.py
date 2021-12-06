"""
reduce(function, iterable[, initializer]) Apply function of two arguments
cumulatively to the items of iterable, reducing the iterable to a single value.

Examples

  >>>reduce(lambda x,y:x+y, range(5))        # sum up numbers from 0 to 4 inclusive i.e. (0+1+2+3+4)
  10
  >>>reduce(lambda x,y:x+y, range(5), 10)    # with initializer set to 10.
  20
  >>>factorial(4)
  24
  >>>factorial(0)
  1
"""
from functools import reduce

def factorial(num):
    """a factorial function using the 'reduce' function"""
    start = 1
    return reduce(lambda a, b: a*b, range(1, num+1), start)


if __name__ == "__main__":
    print(factorial(4))
    print(factorial(10))
    print(factorial(5))
    