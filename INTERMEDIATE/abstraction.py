# =============================== Abstraction =====================================
"""
Abstraction is an OOP Principle in which we hide the internal implementation details and expose only essential functionality to the user.

In simple words,
You show the user what an object can do, without requiring them to know how it does it internally.

For example:
1. You insert your card into the ATM
2. Enter Your Pin
3. Enter the amount to withdraw or deposit
4. Recieve Your cash or deposit

But you don't need to know how the ATM:
1. connects to your bank server
2. Verifies Your Pin
3. Checks your account balance
4. Communicates with the cash dispenser or depositor.


In order to achieve abstraction in Python we use the 'abc' module provided by it.
'abc' stands for the Abstract Base Class.

It allows us to create:
1. Abstract classes
2. Abstract Method.

Q. What is an abstract class?
-> An abstract class is a class that is designed to act as a blueprint for other classes.
-> It is not meant to be instantiated directly when it contains abstract methods.

Q. What is an abstract method?
-> An abstract method is a method declared in an abstract class but without a concrete implementation there.
-> It tells child classes:
    You must provide your own implementation of this method.

For example:
"""

from abc import ABC, abstractmethod

# class BankAccount(ABC):  # Abstract Class (CHild Class)
#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod
#     def deposit(self, amount):
#         pass


# account1 = BankAccount()  # TypeError


# class SavingsAccount(BankAccount):
#     def withdraw(self, amount, name):
#         print(amount, name)


# account = SavingsAccount()
# account.withdraw(1000, "Maaz")


# Important: You cannot directly create and object of this above abstract class as it is meant as the blueprint for all child classes and they must implement their own definitons of abstract methods.

# account = BankAccount()  # Raises a TypeError

"""
Abstraction has two important aspects
A. Hiding the implementation details.
The user interacts with a simple interface without needing to understand the internal working.

B. Enforcing a contract
We define what functionality a class must provide, without deciding exactly how every class must implement it.

In Python OOP, abstract class and abstract methods primarily help us with the second aspect.
They also help us design interfaces that support the first aspect.

Q. What is an interface?
-> An interface is a set of operations that an object promises to provide, without specifying how those operations are implemented.

In simple words,
An interface tells us WHAT an object can do, not how it does it.
"""


class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print(f"Depositing into savings account: {amount}")

    def withdraw(self, amount):
        print("Applying savings withdrawal rules.")

    def check_balance(self):
        print("Checking savings balance.")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        print(f"Depositing into current account: {amount}")

    def withdraw(self, amount):
        print("Applying current withdrawal rules.")

    def check_balance(self):
        print("Checking current balance.")


def perform_withdrawal(account, amount):  # account: savings, amount: 1000
    account.withdraw(amount)
    # savings.withdraw(1000)


savings = SavingsAccount()
current = CurrentAccount()

perform_withdrawal(savings, 1000)
perform_withdrawal(current, 500)
