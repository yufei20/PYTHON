### ======================= Polymorphism ===================

"""
POLYMORPHISM: 
it means method have same same but different logic inside, so each object behaves deifferently.

can be implemented in these 5 ways, there are more ways but most commnly used concept
1. method over riding
2. method overloading
3. operator overloading
4. duck typing
5. function overloading"""
==================================
"""
1. The word polymorphism means 'many forms'.
2. In python, polymorphism allows us to use the same method name or interface for different objects, where each object can behave differently.

For example, Imagine we have three types of bank accounts:
1. Savings Account
2. Current Account
3. Fixed Deposit Account

All three have a method called 'calculate_interest()', but each calculates interest differently.
That is called polymorphism.
Types of techniques to apply Polymorphism:
1. Method Overriding
2. Method Overloading
3. Operator Overloading
4. Duck Typing
5. Function Overloading.
"""

# =================== Method Overriding ========================

"""
=========== Method Overriding (Runtime Polymorphism): =============
Method overriding happens when a child class provide its own implementation of a method that already exists in its parent class.
"""


# class BankAccount:
#     def calculate_interest(self):
#         print("Calculating general bank interest.")


# class SavingsAccount(BankAccount):
#     def calculate_interest(self):
#         print("Savings Interest: 5%")

#     # pass


# class CurrentAccount(BankAccount):
#     def calculate_interest(self):
#         print("Current Account: No interest")


# savings = SavingsAccount()
# current = CurrentAccount()

# savings.calculate_interest()
# current.calculate_interest()

"""
1. Both child classes inherit from BankAccount.
2. Both children have their own calculate_interest() method.
3. When we call the method, Python checks the object's class first.
4. It finds the overridden method and executes that implementation.

This is called method overriding.

Important: The parent method still exists. The child simple provides a different implementation.
"""

# =================== Method Overloading =====================
"""
========= Method overloading (Compile time polymorphism) ============
Method overloading means having multiple methods with the same name but different parameters lists.

For example, in some languages, you can write:
deposit(amount)
deposit(amount, account_type)
deposit(amount, account_type, reference_id)

Each method has the same name but accepts different numbers of arguments.
"""


# Question: Does Python Support Traditional Method Overloading? Let's check:
# class BankAccount:
#     def deposit(self, amount):
#         print("Depositing: ", amount)

#     def deposit(self, amount, bonus):
#         print("Depositing: ", amount + bonus)


# account = BankAccount()
# account.deposit(1000, 500)
# account.deposit(1000)

"""
Does Python Supports Tradition Method Overloading?
Answer: No, Python Does not support traditional method overloading by defining multiple methods with the same name in one class.

The second deposit() method replaces the definition of the first one.


Now the question is: How do we achieve similar behaviour in Python?

We use default arguments or variable-length arguments.
"""

# =============== Approach 1: Default Arguments ===================


# class BankAccount:
#     def deposit(self, amount, bonus=0):
#         total = amount + bonus
#         print("Depositing:", total)


# account = BankAccount()
# account.deposit(1000)
# account.deposit(1000, 500)


# =============== Approach 2: *args ===================


# class BankAccount:
#     def deposit(self, *amounts):
#         print(amounts)
#         total = sum(amounts)
#         print("Depositing: ", total)


# account = BankAccount()
# account.deposit(1000)
# account.deposit(1000, 2000, 3000)


# ================= Operator Overloading ===========================
"""
Operator Overloading means giving an operator different behaviour depending on the objects being used.

For example:
"""
# print(10 + 20)
# print(int.__add__(10, 20))

# print("Hello " + "World!")
# print(str.__add__("Hello ", "World"))
"""
The '+' operator adds numbers but joins strings.

Python achieves this using special methods called magic methods or dunder methods.

For example. '+' internally uses '__add__()'.
Let's take an example:
"""


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __add__(self, other):
#         return self.balance + other.balance


# account1 = BankAccount(1000)  # 1000
# account2 = BankAccount(2000)  # 2000
# # TODO 1: Check for the multiple accounts balances in __add__()
# print(account1 + account2)

""" 
When Python sees: account1 + account2
It internally calls: account1.__add__(account2)
"""

"""
Other commonly used operator methods:
1. '+'                             __add__()
2. '-'                             __sub__()
3. '*'                             __mul__()
4. '/'                             __truediv__()
5. '=='                            __eq__()
6. '<'                             __lt__()
7. '>'                             __gt__()
"""

# ================= Duck Typing ===========================
"""
Duck Typing is a programming concept in Python where an object is treated according to the methods and behaviours it supports, rather than the class it belongs to.

In simple words,
If different objects have the same required  method, we can use a common function to work with all of them, even if they dont inherit from the same parent class.
"""

"""
If it walks like a duck and quacks like a duck , treat it like a duck.
"""


# class SavingsAccount:
#     def withdraw(self):
#         print("Withdrawing From the Savings Account.")


# class CurrentAccount:
#     def withdraw(self):
#         print("Withdrawing from the Current Account.")


# # Third Party Class (Third Person)
# class CryptoWallet:
#     def withdraw(self):
#         print("Withdrawing From the CryptoWallet")


# def process_withdrawal(account):  # crypto
#     account.withdraw()


# savings = SavingsAccount()
# current = CurrentAccount()
# crypto = CryptoWallet()


# process_withdrawal(savings)
# process_withdrawal(current)
# process_withdrawal(crypto)


# ====================== Function Polymorphism ====================
"""
Function polymorphism means that the same function can work with different types of objects or data and perform an appropriate operation depending on the input.
"""

print(len("Python"))
str.__len__("Python")
print(len([1, 2, 3, 4]))
list.__len__([1, 2, 3, 4])
print(len({"name": "Maaz", "age": 23}))
dict.__len__({"name": "Maaz", "age": 23})
