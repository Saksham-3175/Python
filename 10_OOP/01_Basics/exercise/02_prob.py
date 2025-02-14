#Create a Class 'Calculator' which is capable of finding square, cube and square root of a given number.

number = int(input('Enter the number: '))

class Calculator():
    def __init__(self, number):
        self.num = number
    
    def get_values(self):
        print(f"The Square of {self.num} is {self.num * self.num}, Cube is {self.num*self.num*self.num} and the Square Root is {self.num ** (1/2)}")

a = Calculator(number)
a.get_values()
