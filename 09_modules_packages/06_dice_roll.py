import random

print("Welcome to the Dice Roll Simulator!")

while True:
    choice = input("Press Enter to roll or type 'q' to quit: ").strip().lower()

    if choice == "q":
        print("Thanks for playing!")
        break

    dice = random.randint(1, 6)

    print("You rolled:", dice)