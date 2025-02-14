# Operator Overloading
class addNums():
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        return self.num1 + num2.num1 
    
a = addNums(5)
b = addNums(10)
print(a+b)