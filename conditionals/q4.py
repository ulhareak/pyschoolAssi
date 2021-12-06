"""
Define a function to determine the standard achieved by a
participant taking a physical fitness test.

The standard is determined based on the individual and
total scores for 3 stations.

Gold	:Pass	Fail
Min. of 4 points for each station, and min. total of 13
Silver : Min. of 3 points for each station, and min. total of 10
Pass : Min. of 2 points for each station, and min. total of 7
Fail : Less than 2 points for any station or total<7
Examples
   >>> Fitness(4,5,4)
   'Gold'
   >>> Fitness(4,4,4)
   'Silver'
   >>> Fitness(1,5,5)
   'Fail'
   >>> Fitness(2,2,5)
   'Pass'
"""
def Fitness(a, b, c):
	total = (a+b+c) ; 
	l = [a, b,c]
	b = ""
	com = False  
	if total >=13:
		com = compare(l , 4)
		b= "Gold" if com else False	
	elif total >=10 :
		com = compare(l , 3)
		b = "Silver" if com else "Fail" 
	elif total >=7:
		com = compare(l , 2)
		b = "Pass" if com else "Fail"
	else:
		b = "Fail"
	return b
		

def compare(l , no):
	b = False ; 
	
	for i in l :
		if i < no :
			b = False
			break
	else:
		b = True
	return b ; 	

print(Fitness(4,5,4))
print(Fitness(4,4,4))
print(Fitness(1,5,5))
print(Fitness(2,2,5))
