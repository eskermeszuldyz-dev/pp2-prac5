# __init__ constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Zhuldyz", 18)
print(p1.name, p1.age)