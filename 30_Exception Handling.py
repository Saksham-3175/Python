#In python error handling is used to handle the errors that occur during the execution of the program so that the program does not stop abruptly.
#For this we use exception handling in python.
#Lets say user enters a string as input. The program will throw an error and then stop then and there. But if the code has some important lines below then they won't be executed.
#Here comes exception handling. We can execute the remaining lines even if there is an error.
#Syntax:
#try:
# multiplication logic
# except:
# code to be executed if an exception occurs. Error in other words.
#Other important lines of code.

#Example
# a = input("Enter a number to print it's multiplication table: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {i * int(a)}")
# except:
#     print("PLEASE ENTER A NUMBER")

# print("Important lines of code....")

#Handling specific type of errors

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("PLEASE ENTER A NUMBER")
# except Exception as e:
#     print(e)
#The above can be used to print the error message like they way a compiler would throw.

#Handling multiple errors
try:
    num2 = int(input("Enter a number: "))
    a = [1, 2, 3]
    print(a[num2])
except ValueError:
    print("PLEASE ENTER A NUMBER")
except IndexError:
    print("Index out of range")

#Handling multiple errors in one except block
try:
    num3 = int(input("Enter a number: "))
    a = [1, 2, 3]
    print(a[num3])
except (ValueError, IndexError):
    print("PLEASE ENTER A NUMBER OR INDEX OUT OF RANGE")

#Look at the documentation for more information on exception handling.
#https://docs.python.org/3/library/exceptions.html
#https://docs.python.org/3/tutorial/errors.html
