"""
Write a function countVowels(word) that takes in a word as
an argument and returns the number of
vowels ('a', 'e', 'i', 'o', 'u') in the word.

Examples

    >>> countVowels('apple')
    2
    >>> countVowels('microsoft')
    3
    >>> countVowels('google')
    3
"""
def count_vowels(word):
    """ it returns the no. of vowels present in word. """
    tup =  ('a', 'e', 'i', 'o', 'u')
    count  = 0
    if bool(word):
        for i in tup:
            count+=word.count(i)
    return count


w=input("Enter word : ")
print("Vowels are : {}".format(count_vowels(w)))
