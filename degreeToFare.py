"""
Write a function to convert temperature from Celsius to Fahrenheit scale.
oC to oF Conversion: Multipy by 9, then divide by 5, then add 32.

Note: Return a string of 2 decimal places.
"""
def Cel2Fah(temp): 
	x = (temp * 9/5)+32 ; 
	return "{:.2f}".format(x) ;


temp = float( input("Enter temp. in Celsius : ")) ; 

print(Cel2Fah(temp)) ; 
