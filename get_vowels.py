"""
Write the function getVowels(word) that takes in a word as
an argument and returns the vowels
('a', 'e', 'i', 'o', 'u') in that word.

Examples

    >>> getVowels("apple")
    ['a', 'e']
    >>> getVowels("Apple")
    ['A', 'e']
    >>> getVowels("Banana")
    ['a', 'a', 'a']
"""
def get_vowels(word):
    """ returns the vivwls present in the word."""
    vow=['a', 'e', 'i', 'o', 'u']
    l_list=[]
    for i in word:
        if i in vow or i.lower() in vow:
            l_list.append(i)
    return l_list

w = input("Enter word : ")
print("Vowels present in word are {}".format(get_vowels(w)))
