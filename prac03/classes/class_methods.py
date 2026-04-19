# Instance methods

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

p1 = Person("Zhuldyz")
p1.greet()