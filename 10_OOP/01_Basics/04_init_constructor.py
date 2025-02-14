#A constuctor is a special method that is called 'automatically' when an object is created.
#The constructor is always named __init__. As these are the dunder methods(dunder means double underscore).
class Employee():
    lang = 'Python'
    salary = '$10,000'
    def __init__(self):
        self.lang
        self.salary
        print('Constructor is called')
Tom = Employee()
Tom.lang = 'Java'
print(Tom.lang, Tom.salary)
#What happened here is that we created a dunder constructor and it got called automatically.


