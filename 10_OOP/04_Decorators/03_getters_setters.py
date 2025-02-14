# Setter decorator is used to add a logic to set the values. Meaning, it's a way to accept or set the values only when a condition is met.

class Coder():
    def __init__(self):
        print("Coder Constructor Called")
        self.skill = 'Python Scripter'
        self.os = 'Linux OS'
        self.editor = 'Vim'
        self._name = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name can't be empty")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
    

    @property
    def details(self):
        return f"{self.name} is a {self.skill} and uses {self.editor} in {self.os} as their source of power."

hacker = Coder()
hacker.name = 'David'
print(hacker.details)