#Palindrome checker
#Taking input and modifying string. 
palinString = input("Enter the string/sentence: ")
palinString = palinString.replace(" ", "").lower()

#reversing the string
reversePalin = palinString[::-1]

#Palindrome checking
if palinString == reversePalin:
    print(f"Found a match! It is palindrome... '{palinString}', '{reversePalin}'")
else:
    print(f"Match not found! Not a palindrome... '{palinString}', '{reversePalin}'")

print("Exiting...")