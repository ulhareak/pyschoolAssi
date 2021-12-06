"""Create a function addNumbers(x) that takes a number as an argument and adds 
all the integers between 1 and the number (inclusive) and returns the total number."""


def addNumbers(num):
    total = 0
    i = 1
    while i <= num:
        total += i
        i += 1
    return total


if __name__ == "__main__":
    print(addNumbers(10))
    print(addNumbers(1))
