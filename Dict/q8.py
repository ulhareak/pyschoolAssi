"""
Write a function reverseLookup(dictionary, value) that takes in a dictionary and a value as
arguments and returns a sorted list of all keys that contains the value. The function will
return an empty list if no match is found.

Examples

    >>>reverseLookup({'a':1, 'b':2, 'c':2}, 1)
    ['a']
    >>>reverseLookup({'a':1, 'b':2, 'c':2}, 2)
    ['b', 'c']
    >>>reverseLookup({'a':1, 'b':2, 'c':2}, 3)
    []
"""


def reverse_lookup(dictn, value):
    """return keys that contains the the given value."""
    l_look = []
    for i in dictn:
        if dictn[i] == value:
            l_look.append(i)
    l_look.sort()
    return l_look


print(reverse_lookup({'a': 1, 'b': 2, 'c': 2}, 1))
print(reverse_lookup({'a': 1, 'b': 2, 'c': 2}, 2))
