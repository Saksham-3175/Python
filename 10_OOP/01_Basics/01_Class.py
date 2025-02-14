class Employee:
    language = 'Python'
    salary = '$10,000'

emp1 = Employee()
emp1.name = 'John'
print(emp1.name, emp1.language, emp1.salary)

emp2 = Employee()
emp2.name = 'Harvey'
emp2.language = 'Law'
print(emp2.name, emp2.language, emp2.salary)
#Here, Employee is the class and emp1 & emp2 are the objects of the class Employee. Language and salary are class attributes and name is an instance(object) attribute.
#One important thing to note, if we want to change the class attribute, we can. Python priortizes instance attribute over class attribute. Python first checks if there's an instance attribute or not.

