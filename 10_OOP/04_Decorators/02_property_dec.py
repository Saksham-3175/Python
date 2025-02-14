# To use a method as an attribute.
# But why? Because, the method can be accessed as data and not as a function.

class Coder():
    def __init__(self):
        print("Coder Constructor Called")
        self.skill = 'Python Scripter'
        self.os = 'Linux OS'
        self.editor = 'Vim'

    @property
    def details(self):
        return f"{self.name} is a {self.skill} and uses {self.editor} in {self.os} as their source of power."

hacker = Coder()
hacker.name = 'David'
print(hacker.details)
#Notice how we don't need to use the () anymore.