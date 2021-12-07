# A function that calls itself is said to be recursive. The creation of recursive functions is a powerful
# technique to solve problem that can be broken down into smaller or simpler form. One common use is to find
# the factorial of a number. The factorial of a number N is simply the number multiplied by the factorial of (N-1).
# Complete the code given below to calculate and returns the factorial of a numeber.


def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(1))
    print(factorial(0))
