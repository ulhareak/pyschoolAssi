"""
Write a function calDistance(x1, y1, x2, y2) to calculate the distance between two points represented by Point 1 (x1, y1) and Point 2 (x2, y2). The formula for calculating distance is given below:
     distance = √ (x2-x1)2 +  (y2-y1)2 

Examples

    >>> calDistance(1, 0, 0, 0)
    1.0
    >>> calDistance(1, 1, 1, 1)
    0.0
    >>> calDistance(0, 0, 1, 1)
    1.4142135623730951
"""

import math 
def calDistance( x1 , y1 , x2 , y2):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)
	

x1 = int(input("x1")) 














