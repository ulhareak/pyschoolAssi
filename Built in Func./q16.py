# pylint: disable=syntax-error
"""
len(s) Return the length (the number of items) of a sequnce (string, tuple or list) or a mapping (dictionary).

Examples

  >>> len('python')                 # string
  6
  >>> len([])                       # empty list
  0
  >>> len((1, 2, 3, 4))             # tuple
  4
  >>> len({'a':1, 'b':2, 'c':3})    # dictionary
  3
  >>> totSize('abc', (1,), [1,2,3])
  7
"""

# Write a function that returns the total size of the arguments.
# Note: *args denotes a variable argument list, represented by a tuple.


def totSize(*args):
    """returns length of all the variable s in list."""
    l = 0
    for i in args:
        l += len(i)
    return l

if __name__=="__main__":
    print(totSize('abc', (1,), [1,2,3]))
    print(totSize('abc', (1,29 ,3,4,5), [1,2,3]))
    