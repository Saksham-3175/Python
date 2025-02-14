#Methods are functions defined inside classes.
inr = '\u20B9'
class Employee:
    role = 'Data Scientist'
    salary = f'{inr}12 LPA (CTC)'
    def getInfo(self):
        print(f'\n{self.name} is a {self.role} and earns {self.salary}')
Jack = Employee()
Jack.name = 'Jack'
Jack.getInfo()
#Here a para meter 'self' is passed to the method. TLDR: self is just a convention used to specifically refer to the instance of the class.
#Jack is the instance of the class Employee.