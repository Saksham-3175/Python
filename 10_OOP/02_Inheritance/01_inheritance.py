"""Inheritance is the way of creating a new class from an existing class.
Here, Employee is the 'Base Class' and 'Programmer' is the derived class.
The traditional way might be to just copy the attributes and methods from one class to another. But cumbersomes might happen if there are a lot of classes and we need to change 'ONE' attribute of the 'Base Class'. To avoid this cumbersome, we use Inheritance."""
# There are 3 types of inheritance: Single, Multiple, Multilevel. What we did above is Single level.

class Employee():
    company = 'NVIDIA'
    salary = '$200,000'
    def getInfo(self):
        print(f'{self.name} works at {self.company} and bills {self.salary} every year')

class Programmer(Employee):
    skill = 'Machine Learning'
    niche = 'Reinforcement learning'
    def program(self):
        print(f'Their core skill is {self.skill} and the strong hand is in {self.niche}')

emp1 = Programmer()
emp1.name = 'Jack'
emp1.getInfo()
emp1.program()