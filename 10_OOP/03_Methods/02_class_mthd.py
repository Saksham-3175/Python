# A way to access 'Class' inside 'Methods' directly.
# Say, you want to use the 'Class' attirbute instead of 'Instance' attribute, @classmethod is the perfect decorator for it.
class Employee():
    Company = 'MICL'
    Salary = '$25,000'

    def __init__(self):
        print("Constructor Sucessfully Called")
    #Before class decorator-- Instance attribute is prioritized.
    @classmethod
    #Afte class decorator-- Class attribute is prioritized.
    def getInfo(cls):
        print(f'The employee works at {cls.Company} for {cls.Salary}')

a = Employee()
a.Salary = '$40,000'
a.getInfo()
