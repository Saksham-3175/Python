# Create a Class Employee and add Salary and Increment Properties to it.
# Write a method 'salaryAfterIncrement' with a property decorator and a setter which changes value of increment as per salary.

class Employee():
    salary = 23
    increment = 0.7

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * self.increment))

    @salaryAfterIncrement.setter
    def getIncrement(self, salary):
        self.incrementValue = ((self.salary / salary) * 100)
        return self.incrementValue

intern = Employee()    

# print(intern.salaryAfterIncrement)
print(intern.getIncrement)

#You can return anything once @property decorator is used.