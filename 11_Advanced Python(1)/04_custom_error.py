a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))

if (b == 0):
    raise ZeroDivisionError ("Python doesn't even let GOD divide any number by zero!!!")
else:
    print(f'The division of {a} and {b} is {a/b}')
