"""
Create a function addNumbers(start, end) that takes in two positive numbers as arguments and returns the sum of all the number between the start and end number (inclusive).

Examples

    >>>addNumbers(3, 7)
    25
    >>>addNumbers(5, 6)
    11

"""


def addNumbers(start, stop):
    """Add the numbers between the given range ."""
    sum = 0
    for i in range(start, stop+1):
        sum += i
    return sum


if __name__ == "__main__":
    print(addNumbers(2, 6))

__name__ = "__main__"
