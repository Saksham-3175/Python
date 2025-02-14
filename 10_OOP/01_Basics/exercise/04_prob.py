# Create a static method in problem 2 
class Calculator():
    def __init__(self, number):
        self.num = number
    
    def get_values(self):
        print(f"The Square of {self.num} is {self.num * self.num}, Cube is {self.num*self.num*self.num} and the Square Root is {self.num ** (1/2)}")
    
    @staticmethod
    def greet():
        print("Hello")

number = int(input('Enter the number: '))
a = Calculator(number)
a.greet()
a.get_values()



