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
