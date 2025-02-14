#Create a Class with a Class attribute 'a'. Create a object form it and set it to 'a' directly using object.a = 0. Does this change the 'Class Attribute'?

class demo():
    a = 5

obj = demo()
print(obj.a)

obj.a = 7
print(obj.a)
print('The Class attribute does not change because we used an instance attribute on the obj object')

