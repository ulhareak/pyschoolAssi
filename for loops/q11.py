"""
Write a function sumOfDigit(number) that takes in a number as argument and returns the sum of the individual digit in the number.

Examples

  >>> sumOfDigit(123)
  6
  >>> sumOfDigit(234)
  9
  >>> sumOfDigit(1000)
  1
  >>> sumOfDigit(1001)
  2
"""


def sumOfDigit(num):
    """Returns the sum of dugits present in a number ."""
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


if __name__ == "__main__":
    print(sumOfDigit(1234))
    print(sumOfDigit(234))
    print(sumOfDigit(1000))

__name__ = "__main__"
