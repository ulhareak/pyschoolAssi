"""
Write a function hasSameContent(t1, t2) that takes in two tuples as arguments and return True if both tuples contain the same items.

Examples

    >>> hasSameContent((1, 2), (1, 2))
    True
    >>> hasSameContent((1, 2), (2, 1))
    True
    >>> hasSameContent((1, 2), (1, 2, 1))
    False
    >>> hasSameContent((1, 2), ())
    False
"""
def hasSameContent(t1, t2): 
	b= False
	
	if len(t1) != len(t2):
		return False
	
	s1=set(t1)
	s2=set(t2)
	
	return False if bool(s1^s2) else True

print(hasSameContent((1,2),(1,2)))
print(hasSameContent((1,2),(2,1)))
print(hasSameContent((1,2),(1,2,3)))

