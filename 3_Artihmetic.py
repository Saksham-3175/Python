#A basic program of arithmetic operations using input function and type casting.

#Welcome line.
print('Hello user, Enter numbers below:\n')

#Taking input from user.
num1 = input('Enter the first number:')
num2 = input('Enter the second number:')

#To avoid error, we typecast the input(String) into integer value.

#Function to print the arithmetic operations.
def arithmetic_ops(num1, num2):
 print("Performing arithmetic operations on the numbers...\n")
 print(f"Sum = {int(num1) + int(num2)}")
 print(f"Difference = {int(num1) - int(num2)}")
 print(f"Product = {int(num1) * int(num2)}")  
 print(f"Division = {float(num1) / float(num2)}")
 print(f"Exponential = {int(num1) ** int( num2)}")
 print(f"Modulus = {float(num1) % float(num2)}")

#Calling the function
arithmetic_ops(num1, num2)
#End of the code ^_^
