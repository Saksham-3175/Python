#Map function- applys a function to an input list

numbers = [1, 2, 3, 4, 5]
print(numbers)
square = lambda x : x*x

squared_list = map(square, numbers)
squared_list = list(squared_list)
print(squared_list)
#Refer the deepseek chat

#Filter- will give you a filtered output
# A list to get only square of even nubmers
def getEven(n):
    if (n % 2 == 0):
        return True
    return False

even_squared_list = filter(getEven, squared_list)
print(list(even_squared_list))

#Reduce funciton- will give you a single output as it reduces the list to a single value

from functools import reduce
def add(x, y):
    return x + y

sum = reduce(add, numbers)
print(sum)

mul = reduce(lambda x, y : x*y, numbers)
print(mul)

#What's happenening here is- 1+2=3, 3+3=6, 6+4=10, 10+5 = 15
#This is called sequential computation.