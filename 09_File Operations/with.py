# Closing a file is pretty much like adding an indent in python. If not done, it will create a cumbersome; with the 'with' statement you can automatically close the file without explicitly closing it.

# file = open("with.txt")

with open('with.txt') as file:
    read = file.readlines()
    print(read)
print('Closed the file through with statement.')