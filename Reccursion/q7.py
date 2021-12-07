"""
# Write a recursive function countX that takes in a string and returns the number
# of uppercase character 'X' in the String.
"""


def countX(s):
    """Retunrs count of uppercase chars in string."""
    if(len(s) < 1):
        return 0
    else:
        count = 0
        if(s[0] == 'X'):
            count += 1
        return count+countX(s[1:])


if __name__ == "__main__":
    print(countX('aXxXa'))
    print(countX('aaXaXaax'))
    print(countX('xx'))
