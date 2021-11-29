"""
Write a function isEquilateral(x, y, z) that accepts the 3 sides of a triangle as arguments. The program should return True if it is an equilateral triangle.

Examples

    >>> isEquilateral(2, 4, 3)
    False
    >>> isEquilateral(3, 3, 3)
    True
    >>> isEquilateral(-3, -3, -3)
    False
    
"""
def isEquilateral(*l): 
	
	for i in l :
		if i < 0 :
			return False 
	
	if l[0]==l[1] and l[1]==l[2]:
		return True
	else :
		return False 

print("Enter sides of Triangle : ")
l = [] 
for i in range(3):
	l.append(int(input(str(i+1)+"st side :"))) ; 


print(isEquilateral(l[0] , l[1] , l[2])) ;


