"""
Write a function addNumbersInList(numbers) to add all the numbers in a list. To access each element in a list, you can use the statement 'for num in numbers:'.

Examples

  >>> addNumbersInList([])
  0
  >>> addNumbersInList([10, 20, 30])
  60
  >>> addNumbersInList([-10, -20, 30])
  0
"""

def addNumbersInList(numbers): 
	add  = 0 ;
	for i in numbers:
		add +=i ; 
	return add 

no = int(input("Enter how many number you want : "))
l = []
for i in range(no):
	l.append(int(input(str(i+1)+"st number in list : ")))  ; 


print(addNumbersInList(l)) ; 












	
	
	
