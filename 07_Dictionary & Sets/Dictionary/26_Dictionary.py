#Dictionary in python.
#Dictionary is a collection of key-value pairs.
#Dictionary is mutable.
#Dictionary is unordered.
#Dictionary is defined by curly braces {}.
#With dictionairs we can create mapping.
#Creating a dictionary.
dict1 = {'name':'John', 'age':25, 'city':'New York'}
print(dict1)

#printing multiple keys in dictionary
print(dict1.keys())

#printing multiple values in dictionary
print(dict1.values())

#Accessing elements in dictionary
for key in dict1:
    print(key, dict1[key])

#There are 2 ways to access elements in dictionary.
#1.Using get() method.
#2.Using square brackets [].
print(dict1.get('name')) #The get() method returns the value of the specified key and returns None if the key is not found.
print(dict1['name']) #This will throw an error if the key is not found.
#Always use get() method to access elements in dictionary.

print(dict1.items()) #This will return a list of tuples.

for key, value in dict1.items():
    print(key, value)