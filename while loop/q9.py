"""Create a function that takes in a positive number and return 2 integers such that the
number is between the squares of the 2 integers. It returns the same integer twice if the number
is a square of an integer."""


def sqApprox(num):
    i = 0
    minsq = 0                        # set lower bound
    maxsq = num                        # set upper bound
    while i < maxsq:                       # set 'while' termination condition
        if i*i <= num and i > minsq:  # complete inequality condition
            minsq = i
        if i*i >= num and i < maxsq:  # complete inequality condition
            maxsq = i
        i += 1                         # update i so that 'while' will terminate
    return (minsq, maxsq)


if __name__ == "__main__":
    print(sqApprox(2))
    print(sqApprox(4))
    print(sqApprox(5.1))
