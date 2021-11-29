"""
lambda can be considered to be an anonymous and/or inline function. It takes the form of "lambda args : expression."

Examples

    >>> add = lambda x,y:x+y
    >>> add(3, 4)
    7
    >>> even(5)
    False
    >>> even(8)
    True

# Complete the 'lambda' expression so that it returns True if the argument is an even number, and False otherwise.

 
 """
 
even = lambda x : True if x%2 == 0 else False

print(even(int(input("Enter no : ")))) ;  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
