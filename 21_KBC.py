#Simple KBC game in python

#A list containing questions, options and answers.
questions = [
    ["What is capital of India?", "Mumbai", "Delhi", "Chennai", "Banglore", 2],
    ["What is capital of France?", "Mumbai", "Delhi", "Chennai", "Paris", 4],
    ["What is capital of Japan?", "Tokyo", "Delhi", "Chennai", "Banglore", 1],
    ["What is capital of Australia?", "Mumbai", "Delhi", "Sydney", "Banglore", 3],
    ["What is capital of UAE?", "Dubai", "Tehran", "Argentina", "Abu Dhabhi", 2],
    ["What is fullform of FBI?", "Federal Bureau of Investigation", "France Board of Interrogation", "Finland Board of Immigration", "Federal Board of Investigation", 1],
    ["Who invented python?", "Louis Vitton", "Guido Van Russom", "Daniel Mitch", "Linus Torvalds", 2],
    ["In what language is most of the OS written in?", "C", "Java", "Python", "HTML", 1],
    ["Which of the following is used in the backend of web dev?", "Python", "Kotlin", "HTML", "CSS", 1],
    ["You want to do code a operation in python where you don't know how many times the progrom will be recieving the input. What will you use?", "For loop", "Dictionary", "Match Case", "While loop", 4]
            ] 
#A list containing level/amount of the question.
level = [1000, 2000, 5000, 10000, 25000, 100000, 320000, 500000, 5000000, 10000000]

#variable for keeping a track of money won
money = 0

#Loop to print question, take input
for i in range(0, len(questions)):
    question = questions[i]
    
    #printing amount of question
    print(f"Question for Rs. {level[i]}\n")
    
    #Printing the question
    print(question[i])
    
    #Printing the options
    print(f"1. {question[1]}        2. {question[2]}")
    print(f"3. {question[3]}       4. {question[4]}")

    #taking reply and checking it.
    reply = int(input("\nEnter the Option: "))
    if (reply == question[-1]):
     print(f"Correct Answer, you have won Rs. {level[i]}\n")

    else:
     print("Wrong answer")
     break

        #condition for syncing money with level
    if i == 3:
            money = 10000
    elif i == 6:
            money = 320000
    elif i == 9:
            money = 10000000
    

    #Final money after the game
print(f"You are taking Rs. {money} with you!!!")

