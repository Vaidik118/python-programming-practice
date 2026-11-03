# 01_class_and_object.py

class Student:
    def __init__(self, name, roll_number, age):
        self.name = name
        self.roll_number = roll_number
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Age:", self.age)
        print()


student1 = Student("Vaidik", 1, 21)
student2 = Student("Amit", 2, 22)

student1.display()
student2.display()