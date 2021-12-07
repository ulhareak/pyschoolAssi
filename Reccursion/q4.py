"""
# The greatest common divisor (gcd) of 2 or more non-zero integers, is the largest
# positive integer that divides
# the numbers without a remainder. Write a function to compute the gcd of 2 integers
# using Euclid's algorithm:
# gcd(a,0)=a
# gcd(a,b)=gcd(b,a%b)
"""


def gcd(a, b):
    """Returns gcd of numbers"""
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(84, 18))
    print(gcd(112, 42))
    print(gcd(5, 4))
