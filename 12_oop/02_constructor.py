# 02_constructor.py

class Student:
    def __init__(self, roll_number, name, age):
        self.roll_number = roll_number
        self.name = name
        self.age = age

    def display(self):
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Age:", self.age)
        print()


student1 = Student(1, "Vaidik", 21)
student2 = Student(2, "Amit", 22)

student1.display()
student2.display()