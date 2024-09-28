#Arguments in functions:-
#1) Default Arguments- Arguments given to the function by default. If no value is provided during function call, the default value is used. If we provide a value during call, the default value is overwritten.
#                      eg: def add(a = 12, b = 2):
#2) Keyword Arguments- Arguments are passed to the function by keywords irrespective of the order of the arguments.
#                      eg: def add(a, b):
#                          print(a+b)
#                          add(b = 2, a = 12)
#3) Required Arguments- Arguments that are required to be passed during function call. If not passed, it will throw an error.
#                      eg: def add(a, b):
#                          print(a+b)
#                          add(12)
#                         Error: add() missing 1 required positional argument: 'b'
#4) Variable Length Arguments- Arguments that are passed to the function in the form of tuples or dictionaries.
#                      eg: def add(*args):
#                          print(args)
#                          add(1, 2, 3, 4)
#                          Output: (1, 2, 3, 4)
#                      eg: def add(**kwargs):
#                          print(kwargs)
#                          add(a = 1, b = 2, c = 3)
#                          Output: {'a': 1, 'b': 2, 'c': 3}
#5) Anonymous Functions- Functions that are defined without a name. They are defined using the lambda keyword.
#                      eg: add = lambda a, b: a+b
#                          print(add(12, 2))
#                          Output: 14

#Default Arguments
# def add(a = 12, b = 2):
#     print(f"Sum of {a} and {b} is {a+b}")

# print('Default Arguments')
# add()
# add(10)

#Keyword Arguments
# print('Keyword Arguments')
# def add(a, b):
#     print(a-b)
# add(b = 2, a = 12)

#Required Arguments
# print('Required Arguments')
# def add(a, b):
#     print(a+b)

# add(a=1)
#error

#Variable Length Arguments
# average of n numbers
print('Variable Length Arguments\nType: Tuple')
def average(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(f"The average of numbers is {sum/len(numbers)}")
average(1, 2, 3, 4)

print('VLA\nType: Dictionary')
def name(**name):
    print("Hello", name["fname"], name["lname"])

name(fname = "Saksham", lname = "Shukla")

