import random

# Generate a secret number
secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    if guess == secret_number:
        print("Congratulations! You won.")
        break
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")