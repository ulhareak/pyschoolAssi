"""
Write a function addOddNumbers(numbers) to add all the odd numbers in a list. To access each element in a list, you can use the statement 'for num in numbers:'.

Examples

  >>> addOddNumbers([1, 4, 8, 9])
  10
  >>> addOddNumbers(range(1, 20, 3))
  40
  >>> addOddNumbers([])
  0
"""
def addOddNumbers(numbers): 
	add = 0 ;
	numbers = list(numbers)
	for i in numbers:
		if i%2 != 0 :
			add+=i	 ; 
	return add


no = int(input("Enter how many number you want : "))
l = []
for i in range(no):
	l.append(int(input(str(i+1)+"st number in list : ")))  ; 


print("Odd numbers Addition is : {}".format(addOddNumbers(l))) ; 

