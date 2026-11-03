import random

secret_number = random.randint(1, 50)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 50:
            print("Enter a number between 1 and 50.")
            continue

    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! The number was {secret_number}.")
        print(f"You guessed correctly in {attempts} attempts!")
        break