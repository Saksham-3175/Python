#Match case
#The match case statement is a new feature in Python 3.10. It is used to compare the value of a variable with multiple values. The match case statement is similar to the switch statement in other programming languages.
#The match case statement is used to compare the value of a variable with multiple values. The match case statement is similar to the switch statement in other programming languages.
#Just like in swithch statement we add break; in python we use case _ to break the statement.
#Example:  
num = int(input("Enter a number between 1 to 30: "))
match num:
    case 0:
        print(f"Number entered was {num}")
    case _ if num>0 and num <= 10:
        print("Number is positive and ranges between 1 to 10.")
    case _ if num>10 and num <= 20:
        print("Number is positive and ranges between 11 to 20.")
    case _:
        if num<0:
            print(f"{num} is a negative number.")

#Create a program to check the grades of students during the examination. If a paper is finished store the grades in a list and display it so that the student can check their grades of the exam they have appeared for and improve their performance for the next exam.
#The grading system should be as follows:
#Marks between 0-40: Grade F
#Marks between 41-60: Grade D
#Marks between 61-80: Grade C
#Marks between 81-90: Grade B
#Marks between 91-100: Grade A
#Use all the topics learned in the previous programs to create this program.
#Pseudo code:
#1. Create a list to store the grades of the students.
#2. Create a function to check the grades of the students.
#3. Take the input of the marks of the students.
#4. Check the grades of the students.
#5. Store the grades in the list.
#6. Display the grades of the students.

