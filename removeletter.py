"""
Write a function removeLetter(word, letter) that takes in
a word and a letter as arguments and remove all the
occurrence of that particular letter from the word.
The function will returns the remaining leters in the word.

Examples

    >>> removeLetter("apple", "p")
    'ale'
    >>> removeLetter("microsoft", "o")
    'micrsft'
    >>> removeLetter("google", "g")
    'oole'
"""

def remove_letter(word, letter):
    """Removes the given letter from the string"""
    return word.replace(letter,"")

w = input("Enter word:")
l = input("Enter letter :")

print("replaced word are {}".format(remove_letter(w , l)))
