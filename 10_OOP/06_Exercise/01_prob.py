# Create a class 2-D vector and use it to create another class representing a 3-D vector.
class TwoDVector():
    def __init__(self, i, j):
        self.i =  i
        self.j = j
    @property
    def show(self):
        return f"{self.i}i + {self.j}j"
    
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    @property
    def show(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v2d = TwoDVector(1, 2)
print(v2d.show)
v3d = ThreeDVector(1, 2, 3)
print(v3d.show)