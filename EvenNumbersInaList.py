
"""
Write a function getEvenNumbers(numbers) to return all the even numbers in a list.

Examples

  >>> getEvenNumbers([1, 4, 8, 9])
  [4, 8]
  >>> getEvenNumbers(range(1, 20, 3))
  [4, 10, 16]
  >>> getEvenNumbers([])
  []
"""
def getEvenNumbers(numbers): 
	even = [] 
	for i in numbers :
		if i%2 == 0 :
			even.append(i) ; 
	return even ; 

no = int(input("Enter how many number you want : "))
l = []
for i in range(no):
	l.append(int(input(str(i+1)+"st number in list : ")))  ; 


print("Even numbers in a list are : {}".format(getEvenNumbers(l))) ; 



