#A basic program of arithmetic operations using input function and type casting.
print('Hello user, Enter numbers below:\n')

num1 = input('Enter the first number:')
num2 = input('Enter the second number:')

# An error will occur if not typecasted the input function to integer. 
sum = int(num1) + int(num2)
difference = int(num1) - int(num2) 
product = int(num1) * int(num2)  
division = float(num1) / float(num2)
exponential = int(num1) ** int( num2)
modulus = float(num1) % float(num2)

print('The sum of the number is: ', sum)
print('The difference of the number is: ', difference)
print('The product of the numbers is: ', product)
print('The division of the numbers is : ', division)
print('The exponential of the numbers is: ', exponential)
print('The modulus of the numbers is: ', modulus)
