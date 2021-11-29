"""
In Python, it is possible to pass a function as a argument to another function. Write a function useFunction(func, num) that takes in a function and a number as arguments. The useFunction should produce the output shown in the examples given below.

Examples

    >>> def addOne(x):
            return x + 1
    >>> useFunction(addOne, 4)
    25
    >>> useFunction(addOne, 9)
    100
    >>> useFunction(addOne, 0)
    1
"""
def addOne(x):
        return x + 1
        
def useFunction(func, num): 
	num  = func(num)  ;
	return num*num


print("putput is : {}".format(useFunction( addOne,int(input("Enter number : "))))) ; 



    
