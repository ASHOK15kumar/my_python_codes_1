class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable (hidden)

    def get_balance(self):         # getter
        return self.__balance

    def deposit(self, amount):     # setter-like method
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

# Usage
account = BankAccount(1000)

# You can't do this (Python blocks it):
# account.__balance = 5000   # ❌ Not allowed

print(account.get_balance())  # ✔ Allowed

account.deposit(500)
print(account.get_balance())
