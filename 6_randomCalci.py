#A random calculator program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2;
subtraction = num1 - num2;
multiplication = num1 * num2;
division = num1/num2 if num2 != 0 else print("Undefined")

print(f"The addition of numbers is: {addition}")
print(f"The subtraction of numbers is: {subtraction}")
print(f"The multiplicaiton of the numbers is: {multiplication}")
print(f"The division of the numbers: {division}")

print("Exiting...")