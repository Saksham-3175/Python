#For loop.
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#Syntax:
# for variable in sequence:
#     block of code
#To print the elements in a single line, use end ="" in the print statement.
#printing the elements of a string using for loop.
# str = "FOR LOOP in PYTHON"
# for string in str:
#     print(string, end = "")

#The for loop used in the below snippet prints the elements of the string one by one.

# str_2 = input("Enter a string: ")
# for str in str_2:
#     print(str)

#nested for loop.
# colors = ["Red", "Green", "Blue"]
# fruits = ["Apple", "Banana", "Mango"]
# for color in colors:
#     for fruit in fruits:
#         print(color, fruit)
#The loop prints the color and fruit combination for each color and fruit in the list.
#The outer loop iterates over the colors list and the inner loop iterates over the fruits list.

#Range function in for loop.
#The range() function generates a sequence of numbers.
#It's like in C/C++ where we use for(i=0; i<10; i++) to iterate over a sequence of numbers.

#Printing the numbers.
# for i in range(10):
#     print(i)
    # if i == 4:
        # print("The number is 4, exiting the loop.")
        # break

# for a in range(20):
#     print(a + 1, end = " ") 


# for a in range(1, 21):
#     if a%5 == 0:
#         print(a)
#         print(f"{a} is divisible by 5.")
#     else:
#         print(f"{a} *")
#The above loop prints the numbers from 1 to 20 and checks if the number is divisible by 5.

#Range parameters.
#The range() function can take three parameters.
#The first parameter is the starting point.
#The second parameter is the ending point.
#The third parameter is the step value.
    #The step value is the increment value/decrement value.
    #To put in simple words, it just adds the value to the starting point.
# for i in range(1, 21, 2):
#     print (i, end = " ")

#for with else.
#The else block is executed when the loop is exhausted.
#The else block is not executed if the loop is terminated by a break statement.
# for i in range(1, 11):
#     print(i)
# else:
#     print("The loop is exhausted.")
#Exhausted means the loop is completed without any break statement.
#If a break statement is used, the else block is not executed.
# for a in range(1,11):
#     input_1 = int(input("Enter a number: "))
#     if input_1 == 5 or 13 or 17:
#         break
#     else:
#         print("Loop executed sucessfully.")

# for b in range(1, 11):
#     input_2 = int(input("Enter a numbber: "))
#     if input_2 == 1:
#         print("100%")
#     elif input_2 == 7 or 8 or 9:
#     else:
#         print("45%")
#         for B in range(1,11):
#             print(B, end = " ")
#         break
#         for C in range(1,11):
#             print(C, end = " ")

#Multiplication table using for loop.
# table = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(f"{table} * {i} = {table*i}")

    
