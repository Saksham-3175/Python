#Finally keword in python
#Used in exception handling to clean up the code.
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
#Syntax:
#try:
#    code
#except:
#    code
#finally:
#    code

#Example code
# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except:
#     print("Error occured")
# finally:
#     print("FINALLY")

#Now you can also use some other code like print("finally") as it won't make any difference.
#The main use of finally is seen if this code is wrapped in a function.

def func():
 try:
    num = int(input("Enter a index between 0 and 2: "))
    list = [1, 2, 3]
    print(list[num])
    return 1
 
 except IndexError:
    print("Index out of range")
    return 0
 
 finally:
    print("FINALLY")

func()
#Now, how's this useful?
#Let's say you are working on a project and you have to open a file and read it's contents. If the file is not found then the program will throw an error and stop. So you can use the finally block to close the file. This way you can clean up the code and make it more readable and maintainable. This is the main use of finally keyword in python.

#In many interviews you will be asked to give the use of finally keyword in python.
#So, the answer to that will be:
#It is always executed, meaning that it will always run regardless of the try block raising an error or not



#ZeroDivisionError
# def divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     finally:
#         print("FINALLY")
# print(divide(10, 0))
