"""
Write a function countLetters(word) that takes in a word as argument and returns a
dictionary that counts the number of times each letter appears.

Examples

    >>>countLetters('google')
    {'e': 1, 'g': 2, 'l': 1, 'o': 2}
    >>>countLetters('apple')
    {'a': 1, 'e': 1, 'l': 1, 'p': 2}
    >>>countLetters('')
    {}
"""


def count_letters(word):
    """Returns dictionary of no. letters present in the word ."""
    d_count = {}
    for i in word:
        if i not in d_count.keys():
            d_count[i] = word.count(i)

    return d_count


print(count_letters('google'))
print(count_letters("apple"))
