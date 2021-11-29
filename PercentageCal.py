"""
Write a function percent(value, total) that takes in two numbers as arguments, and returns the percentage value as an integer.

 >>> percent(46, 90)
    51
    >>> percent(51, 51)
    100
    >>> percent(63, 12)
    525
  """
def percent ( value , total ):
	return  int(float(value/ float(total))* 100 )

value = int(input("Enter Value : ")) ;
total = int(input("Enter Total :")) ; 

print( "Precentage is :  {}".format(percent(value , total)))
