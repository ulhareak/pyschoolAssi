"""Create a function factorial(x) that takes an integer and returns the 
product of all the positive integers less than or equal to n.
"""


def factorial(num):
    product = 1
    i = num
    while i > 0:
        product = product*i
        i -= 1

    return product


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(0))
