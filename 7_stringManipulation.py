#String manipulation program
Str = input("Enter the sentence: ")

#Length of string.
print("Length of the sentence: ", len(Str))

#Upper and lower case
print("Uppercase: ", Str.upper())
print("Lower: ", Str.lower())

#Reverse string
print("Reversed sentence: ", Str[::-1])

#replacing vowels
vowels = 'aeiouAEIOU'
newStr = Str
for vowel in vowels:
    newStr = newStr.replace(vowel, "*")
    
print("Sentence with replaced vowels: ", newStr)