"""
Write a function isIsosceles(x, y, z) that accepts the 3 sides of a triangle as inputs. The function should return True if it is an isosceles triangle. An isosceles triangle has 2 equal sides. An equilateral triangle is a special case of isosceles triangle.

Examples

    >>> isIsosceles(2, 4, 3)
    False
    >>> isIsosceles(3, 3, 3)
    True
    >>> isIsosceles(2, 3, 2)
    True
    >>> isIsosceles(-2, 3, -2)
    False
    >>> isIsosceles(0, 0, 2)
    False
"""
def isIsosceles(x, y, z): 
	""" returns of the triangle is Isosceles or not """
	
	l =[x ,y, z]
	for i in l:
		if i <= 0:
			return False
	b = False
	if x==y or y==z or x==z:
		b = True
	else:
		b =False
	return b
	
print(isIsosceles(2,3,10))
print(isIsosceles(2,1,4))
