"""
Create a function generateNumbers(start, end) that takes in two numbers as arguments
and returns a list of numbers starting from start to the end number (inclusive)
specified in the arguments. Note: The function range(x, y) can takes in 2 arguments.
For example, range(1, 5) will return a list of numbers [1,2,3,4].

Examples

    >>>generateNumber(2, 7)
    [2, 3, 4, 5, 6, 7]
    >>>generateNumber(1, 1)
    [1]
"""


def generateNumber(start, end):
    """generate numbers from given start and end pos"""
    l_final = []
    for i_num in range(start, end+1):
        l_final.append(i_num)
    return l_final


if __name__ == "__main__":
    print(generateNumber(2, 7))
    print(generateNumber(4, 12))

__name__="__main__"