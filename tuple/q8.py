"""
Write a function shiftByTwo(*args) that takes in variable-length
 argument and returns a tuple with its elements shifted to the
 right by two indices. See samples given below.

Examples

    >>> shiftByTwo(1,2,3,4,5,6)
    (5, 6, 1, 2, 3, 4)
    >>> shiftByTwo('a','b','c','d')
    ('c', 'd', 'a', 'b')
    >>> shiftByTwo('a','b')
    ('a', 'b')
    >>> shiftByTwo('b')
    ('b',)
"""
def shiftByTwo(*args) :
	l1 = args[-2:] +args[:-2] 
	return l1

print(shiftByTwo(1,2,3,4,5,6))
print(shiftByTwo(1,2,3,4,5))


