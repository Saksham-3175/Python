#Functions
#If for some reason you want to write the contents of a function later, you can use thepass keyword.
#Example:
# def funciton_name():
#     pass
#  Code
#(If for some reason you want to use the same function name for different functions, you can use the concept of function overloading.
#Python does not support function overloading. You can define multiple functions with the same name, but they will simply overwrite one another.
#However, you can use default arguments to achieve the same functionality.
#The function below is an example of function overloading.
# def add(a, b):
#     return a + b
#)
#Program to demonstrate a simple calculator using functions.
def add(a, b):
    print(f"{a} + {b} = {a+b:.2f}")
def subtract(a, b):
    print(f"{a} - {b} = {a-b:.2f}")
def divide(a, b):
    print(f"{a} / {b} = {a/b:.2f}")
def multipy(a, b):
    print(f"{a} * {b} = {a*b:.2f}")
def exponential(a, b):
    print(f"{a} ^ {b} = {a**b:.2f}")
def modulus(a, b):
    print(f"{a} % {b} = {a%b:.2f}")

number_1 = float(input("Enter the first number: \n"))
number_2 = float(input("Enter the second number: \n"))

add(number_1, number_2)
subtract(number_1, number_2)
divide(number_1, number_2)
multipy(number_1, number_2)
exponential(number_1, number_2)
modulus(number_1, number_2)


