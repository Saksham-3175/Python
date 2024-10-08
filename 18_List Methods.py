#List methods 
#1. append() - Adds only element at the end of the list.
#2. insert() - Adds an element at the specified position.
#3. clear() - Removes all the elements from the list.
#4. copy() - Returns a copy of the list.
#5. count() - Returns the number of elements with the specified value.
#6. extend() - Adds the elements of one list to another. Pretty much like concatenation or appending lists.
#7. index() - Returns the index of the first element with the specified value.

list = [1, 2, 3, 4, 5]
print(list)

list.append(6)
print("Appended list: ", list)

list.insert(3, 2.5)
print("Inserted value at index 3: ", list)

in_list = list.index(4)
print("Index of 4 in list is: ", in_list)

cp_list = list.copy()
print("Copied list: ", cp_list)

count = list.count(4)
print("Count of 4 in list: ", count)

list.extend([32, 33, 35])
print("Extended list: ", list)

list.clear()
print("Cleared list: ", list)