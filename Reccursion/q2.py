# Write a recursive function power(x, y) to calculate the value of x raised to the power of y.

def power(x, y):
    if(y == 0):
        return 1
    else:
        return x**y


if __name__ == "__main__":
    print(power(5, 2))
    print(power(5, 1))
    print(power(5, 0))
