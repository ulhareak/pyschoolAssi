"""
Define a function isEven(number) that takes in a number
as an argument and returns True if it is an even number.

Examples

    >>> isEven(0)
    True
    >>> isEven(1)
    False
    >>> isEven(-2)
    True
"""


def isEven(x):
    """ Return no is Even or not ."""
    return x % 2 == 0

if __name__ == "__main__":
    print(isEven(10))
    print(isEven(3))
    print(isEven(6))

__name__="__main__"
