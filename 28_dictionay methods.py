#Dictionary methods are very much important as they will be used in mongoDB, Flask, Django.
#They are pretty much same as list and set methods.
#Some methods are:
#1. update() - Updates the dictionary with the specified key-value pairs.
#2. pop() - Removes the element with the specified key.
#3. popitem() - Removes the last inserted key-value pair.
#4. clear() - Removes all the elements from the dictionary.

emp_1 = {'name':'John', 'age':25, 'salary':3500}
emp_2 = {'name':'Smith', 'age':30, 'salary':4500}

#update() method
emp_1.update({'city':'New York'})
print(emp_1)
ep1 = {100: 1, 200: 2, 300: 3}
ep2 = {400: 4, 500: 5, 600: 6}
ep1.update(ep2)
print(ep1)

#pop() method
emp_1.pop('age')
print(emp_1)

#popitem() method
emp_1.popitem()
print(emp_1)

#clear() method
emp_1.clear()
print(emp_1)
#This will return an empty dictionary.

#There are many more methods in dictionary.
#For more methods refer to the official documentation of python.
#https://docs.python.org/3/library/stdtypes.html#dict
