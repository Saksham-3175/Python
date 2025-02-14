class one():
    def __init__(self):
        print('Constructor of class one.')
    a = 1
    @staticmethod
    def greet():
        print("Hello World from class one.")
class two(one):
    def __init__(self):
        super().__init__()
        print('Constructor of class two.')
        # super().greet()
    b = 2
    one.greet() #since greet is a static method, it can be called using the class name without the super() method
class three(two):
    def __init__(self):
        # Call the constructor of the parent class 'two', which in turn calls the constructor of 'one'
        super().__init__()
        print('Constructor of class three.')
    c = 3
o = three()
# print(o.a)
# print(o.a, o.b)
# print(o.a, o.b, o.c)
print(o.c)

#We are calling super().greet() inside the constructor to make sure that the parent class constructor is called first and since it's using self parameter(greet method), calling it inside the constructor ensures that it has the correct context (the class of the object) and can access the method from the parent class correctly.
# Calling greet() outside the constructor may not work because there’s no guarantee the context (self) is available or it might not be properly invoked within an instance context.