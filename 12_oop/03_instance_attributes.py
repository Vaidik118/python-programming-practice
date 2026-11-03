# 03_instance_attributes.py

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print()


employee1 = Employee(101, "Vaidik", 20000)
employee2 = Employee(102, "Amit", 30000)

employee1.display()
employee2.display()

# Modify an instance attribute
employee1.salary = 25000

print("Updated Salary:", employee1.salary)