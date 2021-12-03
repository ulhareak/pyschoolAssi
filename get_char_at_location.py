"""
A string contains a sequence of characters. Elements within
a string can be accessed using index that starts from 0.
Write the function getChar(word, pos) that takes in a word and
a number as argument and returns the character at that position.

Examples

    >>> s = "Hello"
    >>> s[0]
    'H'
    >>> s[-1]
    'o'
    >>> getChar("apple", 2)
    p
    >>> getChar("google", 0)
    g
    >>> getChar("google", 10)
    Invalid Range.
"""
def get_char(word, pos):
    """ Function return char at specified index."""
    return word[pos] if len(word) > pos>= -(len(word)) else "Invalid Range."

w=input("Enter word :")
p=int(input("Enter position:"))
print("char present at pos {} is {}".format(p,get_char(w, p)))
