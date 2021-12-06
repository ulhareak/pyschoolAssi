"""Write a function estimatePi() to estimate and return the value of pi based on the formula
found by an Indian Mathematician Srinivasa Ramanujan. It should use a while loop to compute
the terms of the summation until the last item is smaller than 1e -15. The formula for calculating
distance is given below:
"""


def estimatePi():
    import math

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    return factorial


if __name__ == "__main__":
    print(estimatePi())
