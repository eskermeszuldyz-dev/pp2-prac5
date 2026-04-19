# Class vs instance variables

class Student:
    school = "AITU"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Zhuldyz")
s2 = Student("Ali")

print(s1.name, s1.school)
print(s2.name, s2.school)