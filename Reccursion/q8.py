"""
# Write a recursive function addDashes() that takes in a string and
# returns a new string with all the characters 
# separated by a "-".
"""


def addDashes(s):
    """Add dashesh in the string ."""
    if(len(s) < 1):
        return ''
    elif(len(s) == 0):
        return s[0]
    else:
        return (s[0]+'-'+addDashes(s[1:])).strip("-")


if __name__ =="__main__":
    print(addDashes('google'))
    print(addDashes(''))
    print(addDashes('g'))
