"""Create a function addNumbers(start, end) that adds all the integers
 between the start and end value (inclusive) and returns the total sum."""


def addNumbers(start, end):
    total = 0
    while start <= end:
        total += start
        start += 1
    return total


if __name__ == "__main__":
    print(addNumbers(5, 10))
    print(addNumbers(1, 1))
