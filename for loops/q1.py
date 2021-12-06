"""
Create a function generateNumbers(num) that takes in a positive number as argument and
returns a list of number from 0 to that number inclusive. Note: The function range(5)
will return a list of number [0, 1, 2, 3, 4].

Examples

    >>>generateNumber(1)
    [0, 1]
    >>>generateNumber(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>>generateNumber(0)
    [0]
"""


def generate_number(num):
    """return sequence from 0 to the given number"""
    l_final = []
    for num_list in range(num+1):
        l_final.append(num_list)
    return l_final


if __name__ == "__main__":
    print(generate_number(5))
    print(generate_number(12))
    #print(__name__)

__name__ = "__main__"
