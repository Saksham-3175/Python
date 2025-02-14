#Valrus Operator 

#situation:
# list = [1, 2, 3, 4, 5]
# if len(list) == 3:
#     print('The len of list is 3')
# else:
#     print(f'List is too long: {len(list)} elements, expected <= 3')

#solution:
if ( list := len([1, 2, 3, 4, 5])) >= 3:
    print(f'List is too long, expected less than 3 elements but found {list} elements...')
# TL;DR: This operator helps you to assign values to variables while in an expression.