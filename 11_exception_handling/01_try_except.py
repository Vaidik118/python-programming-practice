# 01_try_except.py

print("Program started.")

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid whole numbers.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

print("Program finished.")