# 02_multiple_exceptions.py

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    numbers = [10, 20, 30]
    index = int(input("Enter list index (0-2): "))

    print("Division:", result)
    print("List value:", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except IndexError:
    print("Error: List index out of range.")

finally:
    print("Program finished.")