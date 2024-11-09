# Strings(sequence of characters).
# Any thing in a single or double quotes is a string in python.

#Defining and printing strings.
lang = "python"
frame = 'django'
print(lang)
print(frame)

#Strings can be concatenated using + operator. To add a space while printing, use ','.
print(lang + frame)
print("python","django")

#The use of quotes in strings.

#Double quotes in single quoted string.
print('He said, "I am learning python"')
#Using escape character to add double quotes in double quoted string.
print("He said, \"I am learning python\"")

#Multi-line string.
multi_string = """He said,
"I am learning python"
and I am loving it """
print(multi_string) 

#String indexing(just like array indexing).
print("lang[3]: ", lang[3]) 
print("lang[-2]: ", lang[-2])

#Using a loop to print slice a multi-line string.
for character in multi_string:
	print(character) 

#String slicing.
str = "Hello Friend"
print("Sliced(0 to 7):", str[0:7])
print("Sliced(5 to end): ", str[5:])
print("The length of the string,", str, "is: ", len(str))

#End of code ^_^