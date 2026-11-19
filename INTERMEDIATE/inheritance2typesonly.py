"""
Inheritance allows a class (child class) to reuse and extend the attributes and methods of another class (parent class).
"""


# Simple Inheritance
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid Amount")
#             return
#         self.balance += amount

#     def withdraw(self, amount):
#         # TODO 1: Conditon check if withdrawal_amount is greater than balance -> error
#         # TODO 2: Condition check if withdrawal_amount is equal to or less than 0 -> error
#         # TODO 3: If withdrawal_amount is equal to balance error.100rs must always reamin in bank account.
#         pass


# class SavingsAccount(BankAccount):
#     def __init__(self, name, balance, age):
#         super().__init__(name, balance)
#         self.age = age

#     def calculate_interest(self):
#         return self.balance * 0.05


# class CurrentAccount(BankAccount):
#     def calculate_charges(self):
#         return 100


# account = SavingsAccount()

# account.deposit(2000)

# print(account.balance)
# print(account.calculate_interest())

# Multiple Inheritance
"""
Multiple inheritance is an OOP concept where a single child class inherits attributes and methods from two or more parent classes.
"""


# class BankAccount:
#     def __init__(self, *, name, balance, **kwargs):
#         self.name = name
#         self.balance = balance
#         super().__init__(**kwargs)

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid Amount")
#             return
#         self.balance += amount


# class SMSAlert:
#     def __init__(self, *, phone, **kwargs):
#         self.phone = phone
#         super().__init__(**kwargs)

#     def send_sms(self):
#         print(f"SMS Notification sent to {self.phone}")


# class test:
#     def __init__(self, age):
#         self.age = age


# class SmartBankAccount(BankAccount, SMSAlert, test):
#     def __init__(self, name, balance, phone, age):
#         super().__init__(name=name, balance=balance, phone=phone, age=age)


# account = SmartBankAccount("Maaz", 4000, "1234", 21)

# account.deposit(1000)
# account.send_sms()
# print(account.balance)


# Multi level inheritance
"""
Multilevel inheritance occurs when a class inherits from another child class, forming a chain of inheritance.
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        self.balance += amount

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, name, balance, interest_rate, cashback_rate):
        super().__init__(name, balance, interest_rate)
        self.cashback_rate = cashback_rate

    def calculate_cashback(self, purchase_amount):
        return purchase_amount * self.cashback_rate / 100


account = PremiumSavingsAccount("Maaz", 4000, 0.01, 0.02)

account.show_details()
print("Interest", account.calculate_interest())
print("Cashback", account.calculate_cashback(20000))
