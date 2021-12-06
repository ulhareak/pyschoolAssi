"""
Write a function that determines if a given year is a leap year.
A leap year is divisible by 4, but not by 100, unless it is also divisible by 400.

Examples

    >>> LeapYear(2012)
    True
    >>> LeapYear(2010)
    False
"""
def LeapYear(yr): 
	""" Return True or False if yr is Lear or not """
	b=True 
	if yr %4 == 0 :
		if yr%100 == 0 :
			if yr %400 == 0 :
				b= True 
			else :
				b= False 
		else :
			b= True 
	else :
		b = False 
	
	return b


print( LeapYear(2010))
print(LeapYear(2012))
