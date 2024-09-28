#String Methods
string = "String methods in Python"
print(string)

#The len() methods returns the length of the string.
print("The length of the string is: ", len(string))

#The lower() method return the string to lower case.
print("Original String:", string)
print("The lower case of the string is: ", string.lower())

#The upper() method returns the string to upper case.
print("Original String:", string)
print("The upper case of the string is: ", string.upper())

#The replace() methods replaces a string with another string.
print("Original String:", string)
print("The replaced string is: ", string.replace("Python", "Django"))

#The split() method splits the string into a list.
print("Original String:", string)
print("The split string is: ", string.split())

#The strip() method removes any whitespace from the beginning or the end.
string2 = "  Stripped string is here "
print("Original String:", string2)
print("The stripped string is: ", string2.strip())

#The capitalize() method capitalizes the first letter of the string. If the first letter is a number, it will not capitalize it. If the first letter is a special character, it will capitalize the next letter. It will change the rest of the string to lower case.

cap_string = "new strIng"
print("Original String:", cap_string);
print("The capitalized string is: ", cap_string.capitalize())

cap_string2 = "_St StRiNg"
print("Origianl string: ", cap_string2)
print("The capitalized string is: ", cap_string2.capitalize())

#The center() method centers the string with the specified width. The default fill character is a space.
center_string = "Centered String"
print("Original String: ", center_string)
print("The length of the string is: ", len(center_string))
print(center_string.center(50))
print(center_string.center(50, "*"))
print("The length of string now is: ", len(center_string.center(40)))

#The count() method returns the number of times a specified value appears in the string.
print("Original String: ", center_string)
print("The number of times 'e' appears in the string is: ", center_string.count("e"))

#The endswith() method returns true if the string ends with the specified value.
print("Original String: ", center_string)
print("The string ends with 'n' is: ", center_string.endswith("n"))
print("The string ends with 'g' is: ", center_string.endswith("g"))

#The startswith() method returns true if the string starts with the specified value.
print("Original String: ", center_string)
print("The string starts with 'C' is: ", center_string.startswith("C"))
print("The string starts with 'c' is: ", center_string.startswith("c"))

#The find() method finds the first occurrence of the specified value. It returns -1 if the value is not found.
print("Original String: ", center_string)
print("The first occurrence of 'e' is at index: ", center_string.find("e"))
print("Is there a 'z' in the string? ", center_string.find("z"))

#Python string methods for bloggers.
#The title() method returns the string with the first letter of each word capitalized.
title_string = "python string methods for bloggers"
print("Original String: ", title_string)
print("The title string is: ", title_string.title())

#The swapcase() method returns the string with the lower case letters converted to upper case and vice versa.
swap_string = "Python String Methods"
print("Original String: ", swap_string)
print("The swapped string is: ", swap_string.swapcase())

#The isalnum() method returns true if all the characters in the string are alphanumeric.
alnum_string = "StringMethods123"
print("Original String: ", alnum_string)
print("Is the string alphanumeric? ", alnum_string.isalnum())
#The isalpha() method returns true if all the characters in the string are alphabetic.

alpha_string = "StringMethods"
print("Original String: ", alpha_string)
print("Is the string alphabetic? ", alpha_string.isalpha())

#The isdigit() method returns true if all the characters in the string are digits.
digit_string = "123456"
print("Original String: ", digit_string)
print("Is the string digits? ", digit_string.isdigit())

#The islower() method returns true if all the characters in the string are lower case.
lower_string = "string methods"
print("Original String: ", lower_string)
print("Is the string lower case? ", lower_string.islower())

#The isupper() method returns true if all the characters in the string are upper case.
upper_string = "STRING METHODS"
print("Original String: ", upper_string)
print("Is the string upper case? ", upper_string.isupper())

#The isspace() method returns true if all the characters in the string are whitespaces.
space_string = "    "
print("Original String: ", space_string)
print("Is the string whitespaces? ", space_string.isspace())

#The join() method joins the elements of an iterable to the end of the string.
join_string = "Python"
print("Original String: ", join_string)
print("The joined string is: ", "-".join(join_string))

#The lstrip() method removes any leading characters (space is the default leading character) from the string.
lstrip_string = "    Python"
print("Original String: ", lstrip_string)
print("The lstrip string is: ", lstrip_string.lstrip())

#The rstrip() method removes any trailing characters (space is the default trailing character) from the string.
rstrip_string = "Python    "
print("Original String: ", rstrip_string)
print("The rstrip string is: ", rstrip_string.rstrip())

#The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
partition_string = "Python is a programming language"
print("Original String: ", partition_string)
print("The partitioned string is: ", partition_string.partition("is"))

#The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
rpartition_string = "Python is a programming language"
print("Original String: ", rpartition_string)
print("The rpartitioned string is: ", rpartition_string.rpartition("is"))










