# First python program.
print('hello world!')

# Type casting in python
a = '1'
b = '2'
print (a + b) # 12

print (int(a) + int(b)) #Typecasting string to int - 3

#Explicit typecasting
string = "15"
number = 10
string_number = int(string) #Typecasting string to int
sum = number + string_number
print(sum)
#output will be 25

#Implicit typecasting
c = 1.8
d = 2
print(c + d) 
#output will be 3.8 as 2 will be converted to float and then added to 1.8

#The key difference between the two is that implicit typecasting is done automatically by the compiler, while explicit typecasting is done manually by the programmer.

#End of code^_^