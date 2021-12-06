"""
Create a function addNumbers(num) that takes in a positive number as argument and returns
the sum of all the number between 0 and that number (inclusive).

Examples

    >>>addNumbers(5)
    15
    >>>addNumbers(0)
    0
"""


def addNumbers(num):
    """ returns addition of numbers in a range i.e ( 0 to num. ) ."""
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def main():
    print(addNumbers(5))
    print(addNumbers(10))

if __name__ == "__main__":
    main()
__name__="__main__"
