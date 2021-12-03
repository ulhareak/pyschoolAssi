"""
Write a function sumNumbers(*args) that takes in a variable-length argument list of numbers and returns the sum of the numbers.
Examples

    >>> sumNumbers(1,2,3,4,5)
    15
    >>> sumNumbers(1,2,3)
    6
    >>> sumNumbers(1)
    1
"""
def sumNumbers (*no):
	sum = 0 
	for i in no :
		sum+=i
	return sum 

print(sumNumbers(1,2,3,4))
print(sumNumbers(4 ,3,2,1))

