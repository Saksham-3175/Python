# Multiple Inheritance is a way to create a 'Child' Class from '2' 'Parent' Classes.
class Employee():
    company = 'Apple'
    salary = '$25,000'
    

class Coder():
    language = 'Python'
    projects = 15
    

class Intern(Employee, Coder):
    def getInfo(self):
        print(f"{self.name} works at {self.company} as a {self.language} Developer Intern with {self.projects} outstanding projects for {self.salary}.")

Newbie= Intern()
Newbie.name = 'Saksham'
Newbie.getInfo()