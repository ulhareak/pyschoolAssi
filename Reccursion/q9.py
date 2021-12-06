"""
# Write a recursive function sumNumbersFromOne(number) that takes
# in a number and returns the sum of all 
# the numbers from one to the number passed in as argument.
"""


def sumNumbersFromOne(x):
    """returns addition of 1 to the given number ."""
    if(x < 1):
        return "Invalid"
    if(x == 1):
        return 1
    else:
        return x+sumNumbersFromOne(x-1)


if __name__ == "__main__":
    print(sumNumbersFromOne(-10))
    print(sumNumbersFromOne(10))
    print(sumNumbersFromOne(5))
