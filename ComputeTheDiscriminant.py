"""
For a quadratic equation in the form of ax2+bx+c, the discriminant, D is b2-4ac. Write a function to compute the discriminant, D.

Examples

    >>> quadratic(1, 2, 3)
    'The discriminant is -8.'
    >>> quadratic(1, 3, 2)
    'The discriminant is 1.'
    >>> quadratic(1, 4, 4)
    'The discriminant is 0.'

"""

def quadratic(a, b, c): 
	d = (b**2)- 4*(a*c) ; 
	return "The discriminant is {}.".format(str(d))  ; 


print("Enter values of a ,b ,c correspondingly : ")
a = int(input("a:")) ; 
b = int(input("b:")) ; 
c = int(input("c:")) ; 


print(quadratic(a ,b ,c))  ;









