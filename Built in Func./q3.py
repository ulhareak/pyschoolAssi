"""# Write a function that returns a string of characters based on a list of ASCII codes."""


def toString(alist):
    """returns string using asci numbers"""

    s = ""
    for i in alist:
        s += chr(i)
    return s


if __name__ == "__main__":
    print(toString([23, 55, 65, 98, 96, 102]))
