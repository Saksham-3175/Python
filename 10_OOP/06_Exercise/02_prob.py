# Create a class Pet from Class Animal and then create a class Dog from Pet. Add a method bark to the Dog class.

class Animal():
    def __init__(self):
        print('Animal Class Constructor')
class Pet(Animal):
    def __init__(self):
        print('Pets Class Constructor')
class Dog(Pet):
    def __init__(self):
        print('Dogs Class Constructor')
    @staticmethod 
    def bark():
        print('Bhowww.... Bhowwww')
ishowspeed = Dog()
print(ishowspeed.bark())
#Classes should always be singular.