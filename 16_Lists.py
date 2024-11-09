#Lists in python are just like arrays in other languages.

list = [1, 2, 3, 4, 5]
print(list)

# list2 = ["Name", "Age", "Gender"]
# print(list2)

#List index - Its just like arrays indexing.
# print(list2[0])
# print(list[0])

#Negative indexing- starts from the end of the list.
#Whenever you get a problem on negative indexing, remember to convert it to positive indexing.
print(list[-3]) #Output: 3 as its the 3rd element from the end of the list.
print("Length of list is",len(list))
print(len(list)- list[-3]) #Output: 3, its the 3rd element from the start of the list.
print(list[3])

#List Slicing- pretty much like string / array slicing.

#To find if the element is present in the list or not.
presentOrNot = [1, "a", 2, "b"]
print(presentOrNot)
if "a" in presentOrNot:
    print("1")
else:
    print("0")

