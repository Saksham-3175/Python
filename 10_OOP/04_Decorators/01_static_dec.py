# To use the methods without self parameter so that unnecesary access of attributes is avoided.
class Programmer():
    lang = 'Python'
    core = 'Lists'
    weak = 'Data Types'
    @staticmethod
    def greet():
        print('Hello From Static Decorator')
    
code = Programmer()
code.greet()