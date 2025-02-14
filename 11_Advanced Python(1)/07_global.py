#The use of global keyword (incorrect code)
def print_number(a):
    # global a
    a = 42
    print(f'The number is {a}')
a = 23523
print_number(a)