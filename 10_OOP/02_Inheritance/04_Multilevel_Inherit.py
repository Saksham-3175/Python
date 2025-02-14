# Multilevel Inheritance is a way of creating a 'second child class' from the 'first child class' and the 'parent class'. Parent_Class -> Child_Class_1 -> Child_Class_2

class one():
    a = 1
class two(one):
    b = 2
class three(two):
    c = 3
o = three()
print(o.a)
print(o.a, o.b)
print(o.a, o.b, o.c)
