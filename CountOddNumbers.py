"""
Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.

Examples

  >>> countOddNumbers([1, 4, 8, 9])
  2
  >>> countOddNumbers(range(1, 20, 3))
  4
  >>> countOddNumbers([])
  0

"""

def countOddNumbers(numbers): 
	count = 0 ; 
	for i in numbers :
		if i%2 != 0 :
			count+=1  ;
	
	return count


no = int(input("Enter how many number you want : "))
l = []
for i in range(no):
	l.append(int(input(str(i+1)+"st number in list : ")))  ; 


print("Odd numbers count is : {}".format(countOddNumbers(l))) ; 









