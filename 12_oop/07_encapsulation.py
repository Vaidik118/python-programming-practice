# 07_encapsulation.py

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Vaidik", 5000)

print("Account Holder:", account.account_holder)
print("Initial Balance:", account.get_balance())

account.deposit(2000)
account.withdraw(1000)

print("Final Balance:", account.get_balance())