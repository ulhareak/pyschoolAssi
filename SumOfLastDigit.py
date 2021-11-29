"""
Write a function getSumOfLastDigits() that takes in a list of positive numbers and returns the sum of all the last digits in the list.

Examples

    >>> getSumOfLastDigits([2, 3, 4])
    9
    >>> getSumOfLastDigits([1, 23, 456])
    10

"""
def getSumOfLastDigits(numList): 
	sum = 0 ; 
	for i in numList:
		sum = sum + (i%10) ; 
	return sum ; 

l = [] ; 
no = int(input("how many no. you want : ")) ; 

for i in range(no):
	l.append(int(input("Enter no  :"))) 

print("The sum of last Digits in a list are : {}".format(getSumOfLastDigits(l))) ; 


