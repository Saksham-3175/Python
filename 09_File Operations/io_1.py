#file reading
# file = open("this.txt")
# data = file.read()
# print(data)
# file.close()

#file writing
# str = "This is a string file"
# file = open("string.txt", "w")
# file.write(str)
# file.close()

#Printing mulitiple lines from a file.
keyboard = open("multiple.txt")
data = keyboard.readline()
#for loop
# for line in data:
#     print(line)
# print(data, type(data))
#while loop
while (data != ""):
    print(data)
    data = keyboard.readline()
keyboard.close()