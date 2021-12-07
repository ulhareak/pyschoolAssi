"""
# Write a function createStars(num) that takes in a number as
# argument and returns a string of stars 2num long.
"""


def createStars(x):
    """it prints the * pattern ."""
    if x == 0:
        return '*'
    else:
        return '*'*2**x


if __name__ == "__main__":
    print(createStars(0))
    print(createStars(1))
    print(createStars(2))
    print(createStars(3))
