#Tuple Methods
# Python has two built-in methods that you can use on tuples.
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Example
# Return the number of times the value 5 appears in the tuple:
thistuple =  (1, 3, 3, 5, 5, 3, 6, 6, 4, 5)
x = thistuple.count(5)
print(f"5 appears {x} times in the tuple")

# Example
# Search for the first occurrence of the value 3, and return its position:
thistuple =  (1, 3, 3, 5, 5, 3, 6, 6, 4, 5)
x = thistuple.index(3)
print(f"3 appears first at position {x} in the tuple")
# Note: The index() method only returns the first occurrence of the value.
# If the value is not found, the index() method raises an exception
# x = thistuple.index(2)
# print(f"2 appears first at position {x} in the tuple")

#Index slicing in tuple:
# Index slicing in tuple is same as list
thattuple = (1,35, 87, 9, 3, 5, 60, 57)
print(thattuple[2:5]) 

# x = thattuple.index(3, 0, 3)
# x is not in tuple for the above
x = thattuple.index(3, 0, 7)
#output: 4
print(x)