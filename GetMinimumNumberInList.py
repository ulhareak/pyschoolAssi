"""
Write a function getMinNumber(numbers) that returns the minimum number in a list.

Examples

  >>> getMinNumber([12, 4, 10])
  4
  >>> getMinNumber([])
  'N.A'


"""
def getMinNumber(numbers): 
	if not bool(numbers):
		return "N.A" 
	else :
		min = numbers[0]
		for i in numbers : 
			if min > i :
				min = i 
	
	return min 
	

no = int(input("Enter how many number you want : "))
l = []
for i in range(no):
	l.append(int(input(str(i+1)+"st number in list : ")))  ; 

print("Minimum number in a list: {}".format(getMinNumber(l))) ; 










