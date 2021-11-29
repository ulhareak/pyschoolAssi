"""
Write a function to compute the BMI of a person.
    BMI = weight(kg)  /  ( height(m)*height(m) )
    
     >>> BMI(63, 1.7)
    '21.8'
    >>> BMI(110, 2)
    '27.5'
    # Note: Return a string of 1 decimal place.
    
   """
def BMI(weight, height): 
	return "%.1f"%( weight / float( height * height)) 
	
w = float( input("Enter Weight : ")) ;
h = float(input("Enter HEight : ")) ;

print(BMI( w , h) ) ; 
