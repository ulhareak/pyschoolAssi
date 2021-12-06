# The Fibonacci numbers are the integer sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ..., in
# which each item is
# formed by adding the previous two. The sequence can be defined
# recursively by the following definition:


# Write a function fibonacci(number) that takes in a number as argument.
# The function should calculate and return
# the fibonacci number for the number passed in.

def fibonacci(number):
    """Prints Fibo series."""
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)


if __name__ == "__main__":
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))
