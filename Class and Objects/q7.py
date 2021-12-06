"""
It is possible to change the behaviour of built-in
opertators with special methtods. For example,
the '+' operator can be implemented
with the __add__ method. Define a Point class that supports
operator overloading for the '+' and '-' operators.

Examples

    >>> a = Point(1,3)     
    >>> b = Point(7,2)     
    >>> print a+b
    '(8, 5)'
    >>> print a-b
    '(-6, 1)'
"""
class Point:
    "A class implementation of 2-Dimensional point."
    def __init__(self,x,y):
         self.x=x
         self.y=y
        
    def __str__(self):
         return '(%d, %d)' % (self.x, self.y)
        
    def __add__(self, other):
      	 return "({}, {})".format(self.x+other.x , self.y+other.y)

    def __sub__(self, other):
      	 return "({}, {})".format(self.x-other.x , self.y-other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1+p2)
print(p1-p2)






