# ============= Composition ======================
"""
Composition is an OOP concept in which one class contains an object of another class as one of its attributes.

In simple words,
One Object is made up of or contains other objects.
It represents a HAS-A relationship between classes.

For example:
* A Bank Account HAS-A Transaction History
* A Car HAS-A Engine
* A Computer HAS-A Processor.

For example:
"""


class TransactionHistory:
    def __init__(self):
        self.transaction = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)

    def show_transactions(self):
        for transaction in self.transaction:
            print(transaction)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.history = TransactionHistory()

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        self.balance += amount
        print(f"Deposited Successfully: {amount}")

        # Objject ot TransactionHisotry
        self.history.add_transaction(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal Successfull\nRemaining Amount: {self.balance}")

        self.history.add_transaction(f"Withdrawan: {amount}")


account = BankAccount(1000)

account.deposit(2000)
account.withdraw(3000)

print("=========================================================")
account.history.show_transactions()
