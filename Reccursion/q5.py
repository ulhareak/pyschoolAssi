"""
# A palindrome is a word, phrase, number or other sequence of units that can
# be read the same way in either 
# direction. Write a recursive function that determines whether the given word is a palindrome.
"""


def isPalindrome(word):
    """Return True or False acco to string is planidrome or not  """
    if(len(word) < 1):
        return True
    else:
        if(word[0].lower() == word[-1].lower()):
            return isPalindrome(word[1:-1])
        else:
            return False


if __name__ == "__main__":
    print(isPalindrome("Racecar"))
    print(isPalindrome("Never"))
    print(isPalindrome("level"))
