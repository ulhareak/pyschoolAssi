"""
The determinant of a 2x2 matrix is the product of the elements on the main diagonal minus the product of the elements off the main diagonal.

Examples

    >>> M = ((3,1), (5,2))
    >>> det(M)
    1
"""
def det(M):
	return abs((M[0][0]*M[1][1])- (M[0][1]*M[1][0]))

t = ((3,1),(5,2))
print(det(t))
