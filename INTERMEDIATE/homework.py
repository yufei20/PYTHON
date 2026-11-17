16 Nov 2026
# ======================== Static Methods ==============================

"""A static method is a method defined inside a class that does not automatically recieve the object (self) or the class (cls) as an argument."""


# class Template:
#     def __init__(self):  # obj
#         pass

#     def calculate_age_from_dob(self, dob):
#         pass

#     @staticmethod
#     def greet(name):
#         pass


# obj = Template()

# Template.calculate_age_from_dob(Template(), "DOB")

# obj.greet()
# Template.greet()


# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b


# print(Calculator.add(10, 20))

# =============== Class Method =====================

"""
A class method is a method that recieves the class as its first argument conventionally named 'cls', rather than recieving a particular object.
"""


class BankAccount:
    bank_name: str = "Python bank"

    @classmethod
    def change_bank_name(cls, new_name: str):  # cls = BankAccount
        cls.bank_name = new_name

    @classmethod
    def display_bank_name(cls):
        print(f"Welcome to {cls.bank_name}")

    @classmethod
    def show_class(cls):
        print(cls)
        print(cls.__name__)


BankAccount.show_class()
===========================

17 november 2026 is completed
1:08 PM
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

