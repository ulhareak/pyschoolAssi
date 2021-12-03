"""
Write the function changeCase(word) that changes the
case of all the letters in a word and returns the new word.

Examples

    >>> changeCase('aPPle')
    "AppLE"
    >>> changeCase('BaNaNa')
    'bAnAnA'
"""

def change_case(word):
    """ Swapint the letters present in the word ."""
    return word.swapcase()

w = input("Enter word:")
print("Swaping case word are {}".format(change_case(w)))
