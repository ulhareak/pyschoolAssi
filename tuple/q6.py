"""
Write a function commonElements(t1, t2) that takes in 2
tuples as arguments and returns a sorted tuple
containing elements that are found in both tuples.

Examples

    >>> commonElements((1, 2, 3), (2, 5, 1))
    (1, 2)
    >>> commonElements((1, 2, 3, 'p', 'n'), (2, 5 ,1, 'p'))
    (1, 2, 'p')
    >>> commonElements((1, 3, 'p', 'n'), ('a', 2 , 5, 1, 'p'))
    (1, 'p')
"""
def commonElements (t1 , t2):
	s1 = set(t1)
	s2 = set(t2)
	s3 = s1.intersection(s2)
	l = list(s3)
	l.sort()
	return tuple(l)

print(commonElements((1,2,3) , (3,4,5)))
print(commonElements((2,1,3) , (2,3,4)))









