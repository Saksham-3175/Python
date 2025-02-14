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