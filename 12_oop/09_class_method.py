# 09_class_method.py

class Student:
    school_name = "ABC School"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", self.school_name)

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def get_student_count(cls):
        return cls.student_count


student1 = Student("Vaidik", 21)
student2 = Student("Amit", 22)

student1.display()

Student.change_school("XYZ School")

print("\nUpdated School:", Student.school_name)
print("Total Students:", Student.get_student_count())