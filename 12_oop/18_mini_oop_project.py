# 18_mini_oop_project.py
# Mini Project: Bank Account Management System


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        self.check_balance()


def main():
    account_holder = input("Enter account holder name: ")

    account = BankAccount(account_holder)

    while True:
        print("\n===== BANK MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == 3:
                account.check_balance()

            elif choice == 4:
                account.display_details()

            elif choice == 5:
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice. Select 1-5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()