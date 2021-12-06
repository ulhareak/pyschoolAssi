"""
Construct a class named 'Point', which takes in the x and
y coordinates as parameters. It should include the documentation string and the methods '__init__' and '__str__'.

Examples

    >>> P1  = Point(2,4)
    >>> P1.__doc__
    'A class implementation of a 2-dimensional point.'
    >>> str(P1)
    '(2, 4)'
    >>> print P1
    (2, 4
"""
class Point:
    """A class implementation of a 2-dimensional point."""
    def __init__(self,   x , y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({}, {})".format(self.x,self.y)
p=Point(10, 20)
print(str(p))
print(p.__doc__)
