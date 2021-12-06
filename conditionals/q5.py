"""
Define a function isPrime(number) that takes in a number as
argument and return True if the number is a prime number.

    Hint: A number, x is a prime number if it is only
    divisible by 1 and x itself.
    By definition, 1 is not a prime number.
Examples
   >>> isPrime(97)
   True
   >>> isPrime(1)
   False
   >>> isPrime(-2)
   False
   
"""
# Hint: Step through the range between (2, number-1), 
# and determine if the number is divisible using the modulus operator.

def isPrime(x):
	""" Returns True or False if the number is Prime or Not """
	#x = 4
	b = True
	if x< 2 :
		b= False 
	else : 
		for i in range(2, int(x/2)+1):
			if x%i==0:
				b = False
				break
	return b 

print(isPrime(97))
print(isPrime(1))
print(isPrime(-2))
