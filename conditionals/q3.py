"""
Write a function isScalene(x, y, z) that accepts the 3 sides of a triangle as inputs. The function should return True if it is a scalene triangle. A scalene triangle has no equal sides.

Examples

    >>> isScalene(2, 4, 3)
    True
    >>> isScalene(3, 3, 3)
    False
    >>> isScalene(2, 2, 3)
    False
"""
def isScalene(x, y, z): 
	f=[x,y,z]
	for i in f:
		if i <= 0 :
			return False
	s1 = set(f)
	b = False
	if len(s1)<3:
		b= False
	else:
		b = True
	return b

print(isScalene(2,1,5))
print(isScalene(4,2,2))
