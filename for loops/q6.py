"""
Create a function addEvenNumbers(start, end) that takes in two positive numbers
as arguments and returns the sum of all the even numbers between the start and
end number (inclusive). Note: x % 2 returns 0 if x is an even number.

Examples

    >>>addEvenNumbers(3, 7)
    10
    >>>addEvenNumbers(5, 12)
    36
"""


def addEvenNumbers(start, stop):
    """Add even numbers between the given range ."""
    sum = 0
    for i in range(start, stop+1):
        if i % 2 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    print(addEvenNumbers(2, 10))
    print(addEvenNumbers(3, 21))

__name__ = "__main__"
