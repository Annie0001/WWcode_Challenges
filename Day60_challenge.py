# Create a class representing a simple bank account with deposit and withdraw methods
class bank_account:
    def __init__(self):
        self.balance = 0

    def deposit(self, dep_amount):
        self.balance = self.balance + dep_amount

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount

    def get_balance(self):
        return self.balance

my_bank_account = bank_account()
my_bank_account.deposit(10)
print(my_bank_account.get_balance())

my_bank_account.withdraw(5)
print(my_bank_account.get_balance())