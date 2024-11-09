#Enumerate function
#To put in simple words, it is used to loop over a container and have an automatic counter.
#Means, it will return the index and the value of the item in the container.

#Basic example

marks = [35, 53, 52, 90, 99, 34]
index = 0
for mark in marks:
    print(mark)
    if mark == 99:
        print("Awesome")
    index += 1
print("\n")

#Enumerate example

marks = [1, 3, 6, 10, 2, 8, 7]
for en, mark in enumerate(marks, start=1):
    print(mark) 
    
    if en == 3:
        print("Awesome")

        