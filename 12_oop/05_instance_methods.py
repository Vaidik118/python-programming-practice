# 05_instance_methods.py

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"

        return self.num1 / self.num2


calculator = Calculator(20, 5)

print("Addition:", calculator.add())
print("Subtraction:", calculator.subtract())
print("Multiplication:", calculator.multiply())
print("Division:", calculator.divide())