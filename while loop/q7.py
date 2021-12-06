"""Create a function doubleFactorial(n) that takes an odd integer and returns 
the product of all odd values up to the value n (where n=2k-1)."""


def doubleFactorial(num):
    product = 1
    i = 0
    k = 1
    while k < num:
        k = 2*i+1
        product *= k
        i += 1
    return product


if __name__ == "__main__":
    print(doubleFactorial(9))
    print(doubleFactorial(1))
