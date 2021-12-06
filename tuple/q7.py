"""
Write a function removeCommonElements(t1, t2) that takes in 2 tuples as arguments and returns a sorted tuple containing elements that are not found in both tuples.

Examples

    >>> removeCommonElements((1,2,3,4), (3,4,5,6))
    (1, 2, 5, 6)
    >>> removeCommonElements(('b','a','c','d'), ('a','b','c'))
    ('d',)
    >>> removeCommonElements(('a','b','c'), ('a','b','c'))
    ()
    >>> removeCommonElements(('a','b'), ('c', 'd'))
    ('a', 'b', 'c', 'd')
    >>> removeCommonElements(('b','a','d','c'), ('a','b'))
    ('c', 'd')
"""
def removeCommonElements(t1,t2):
	s1 = set(t1)
	s2 = set(t2)
	s3 = s1.symmetric_difference(s2)
	l = list(s3)
	l.sort()
	return tuple(l)
	
print(removeCommonElements((1,2,3) , (2,3,4)))
print(removeCommonElements((1,2,3),(3,2,1)))





	
	
