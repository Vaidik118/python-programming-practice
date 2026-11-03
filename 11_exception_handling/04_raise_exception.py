# 04_raise_exception.py

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        raise ValueError("You must be at least 18 years old.")

    print("Access granted!")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as error:
    print("Error:", error)

finally:
    print("Program finished.")