#Conditional statements in python.
#if, elif, nested if-else.
#Indentation is very important in python. It is used to define the block of code.
#eg. if condition:
# (whitespace) block of code
#    else:
#        block of code
#level of indent
#    level of indent
#        level of indent

#1. if-else statement
#Checking the number is positive or negative.
# num = int(input("Enter a number: "))
# if num>0:
#     print(f"{num} is a positive number.")
# else:
#     print(f"{num} is a negative number.")

#2. if-else ladder(if-elif-else)
#Printing the range of number taken as input.
# num = int(input("Enter a number between 1 to 30: "))
# if num>0 and num<=10:
#     print(f"Number({num}) is positive and ranges between 1 to 10.")
# elif num>10 and num<=20:
#     print(f"Number({num}) is positive and ranges between 11 to 20.")
# elif num>20 and num<=30:
#     print(f"Number({num}) is positive and ranges between 21 to 30.")
# elif num == 0:
#     print(f"Number entered was {num}")
# elif num<0:
#     print(f"{num} is a negative number.")
# else:
#     print(f"{num} is not in the range of 1 to 30.")


#3. Nested if-else statement
#Checking the range of number taken as input.
# num = int(input("Enter a number to check if it's greater or less than 3 digits: "))
# if num >= 0:
#     if num == 0:
#         print(f"Number entered was {num}")
#     else:
#         print(f"{num} is a positive number.")
#         if num<100:
#             print(f"{num} is less than 3 digits.")
#         else:
#             print(f"{num} is greater than 3 digits.")
# else:
#     print(f"{num} is a negative number.")


