# 05_custom_exception.py

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")

    print("Access granted!")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError:
    print("Error: Please enter a valid integer.")

except InvalidAgeError as error:
    print("Error:", error)

finally:
    print("Program finished.")