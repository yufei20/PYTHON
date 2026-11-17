
"""
Inheritance allows a class (child class) to reuse and extend the attributes and methods of another class (parent class).
"""


# Simple Inheritance
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        self.balance += amount

    def withdraw(self, amount):
        # TODO 1: Conditon check if withdrawal_amount is greater than balance -> error
        # TODO 2: Condition check if withdrawal_amount is equal to or less than 0 -> error
        # TODO 3: If withdrawal_amount is equal to balance error.100rs must always reamin in bank account.
        if amount >= self.balance or amount > self.balance-100 or amount<=0:
            print("invalid amount")
            return 
        self.balance = self.balance - amount
        

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.05
        


class CurrentAccount(BankAccount):
    def calculate_charges(self):
        return 100


account = SavingsAccount("Maaz", 1000)

account.deposit(2000)

print(account.balance)
print(account.calculate_interest())
print(account.withdraw(500))
print(account.balance)


