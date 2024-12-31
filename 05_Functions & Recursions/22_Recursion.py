#Recursion in python
#Recursion simply means that a function is calling itself.

#FACTORIAL OF A NUMBER
#Defining the function
def factorial(n):
    '''A simple function depicting recursion for factorial of a number.'''
    if (n==1 or n==0):
        return 1
    else:
        return (n* factorial(n-1))

#Printing the docstring and the result    
print(factorial.__doc__)
print(factorial(5))

#FINDING FIBONACCI SEQUENCE 
#Function definition
def fibonacci(n):
    '''A recursive function to compute the fibonnaci sequence.'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Taking input from user    
num = int(input("Enter the number:"))

#Loop to iterrate and print the numbers
for i in range(num):
    print(fibonacci(i))

