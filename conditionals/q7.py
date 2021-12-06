"""
Define a function that takes in 3 values and determine if they can form the sides of an triangle.

    Hint: The sum of the lengths of any two sides of a triangle is
          greater than the length of the third side.
Examples
   >>> isTriangle(3,4,5)
   True
   >>> isTriangle(1,3,1)
   False
"""
def isTriangle(x,y,z):
	""" Returns True or False Acco. to sides can form a triangle or
	not """
	l = [x,y,z]
	s1 = set(l)
	b = False
	if len(s1) == 3:
		if (x+y == z ) or (x+z == y )or (y+z == x):
			b = False
		else :
			b = True
	return b


print(isTriangle(3,4,5))
print(isTriangle(1,3,1))
