#A calculator program at random

#Taking user iput.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#A function for user to display the availabe operations and thier input values
def calci_menu():
    print("0 to Quit.")
    print("1 to Add the numbers.")
    print("2 to Subtract the numbers.")
    print("3 to Multiply the numbers.")
    print("4 to Divide the numbers.")


#Function to print result of operations.
def calci_operation(option):
    match option:
        case 0: 
            print("Quitting...")
            exit
        case 1:
            print(f"Addition of nubmers is: {addition}")
        case 2:
            print(f"The subtraction of numbers is: {subtraction}")
        case 3:
            print(f"The multiplicaiton of the numbers is: {multiplication}")
        case 4:
            print(f"The division of the numbers: {division}")

#Logic of operations.
addition = (num1) + (num2);
subtraction = (num1) - (num2);
multiplication = (num1) * (num2);
division = (num1)/(num2) if (num2) != 0 else print("Undefined")

#Function calling
calci_menu()

#Taking input to perform operation on the numbers.
option = int(input("Enter a specified number to perform the operation: "))

calci_operation(option)

# print(f"The addition of numbers is: {addition}")
# print(f"The subtraction of numbers is: {subtraction}")
# print(f"The multiplicaiton of the numbers is: {multiplication}")
# print(f"The division of the numbers: {division}")
# print("Exiting...")