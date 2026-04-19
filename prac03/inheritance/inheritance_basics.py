# Basic inheritance

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()