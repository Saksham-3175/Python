#Static method is used when we don't want to access the instance or class attributes. It is a decorator(upcoming code file)

class Employee():
    lang = 'Python'
    salary = '$10,000'
    @staticmethod
    def greet():
        print('Happy Coding!!!')
Tom = Employee()
Tom.greet()

#Static method can also be used to get class attributes
#Ex_1
class Employee():
    lang = 'Python'
    salary = '$10,000'
    @staticmethod
    def greet():
        print(f'Happy Coding in {Employee.lang}!!!')

Jimmy = Employee()
Jimmy.greet()

#Ex_2
class Demo:
    class_count = 10
    def __init__(self, value):
        self.value = value

    @staticmethod
    def show_class_count():
        print(f"Class Count: {Demo.class_count}")

obj = Demo(5)
obj.show_class_count()