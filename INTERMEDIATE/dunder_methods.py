# ========================= Dunder Methods =================================
"""
Dunder methods stand for Double underscore

Dunder methods are special methods in Python that have double underscores before and after their names.

For example:
__init__() # constructor
__str__()
__len__()
__add__()

They are also called as Magic Methods.

Python already provides some builtin operations, such as:
1. '+' to add values, __add__()
2. '==' to compare values, __eq__()
3. 'len()' to find the length, __len__()
4. 'print()' to display something.

Dunder methods allows us to define how these operations should behave when used with our own objects.
"""


# =============== First example: __str__() for users ==============================
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# account = BankAccount("Maaz", 4000)
# print(account) # account.__str__()


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         # print(f"Account Holder: {self.owner}, Balance: {self.balance}")
#         return f"Account Holder: {self.owner}, Balance: {self.balance}"


# account = BankAccount("Maaz", 4000)
# print(account)  # account.__str__()

"""
When you write print(account), Python internally calls account.__str__()
Remember: __str__() must return a string, not print one.
"""


# =========================== __repr__(): Developer Friendly Representation ================================
"""
It defines how an object should be represented when we're inspecting or debugging it as developers.
"""


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __repr__(self):
#         return f"BankAccount(owner='{self.owner}', balance={self.balance})"


# account = BankAccount("Maaz", 4000)
# print(repr(account))  # account.__repr__(), account.__str__()

# print(repr(FastAPI))

# ====================== __len__(): Custom Length of an object =============================
"""
__len__() allows us to define what the built in len() function should return when it is used with our custom objects.
"""


# class TransactionHistory:
#     def __init__(self):
#         self.transactions = []  # Empty List

#     def add_transaction(self, transaction):
#         self.transactions.append(transaction)

#     def __len__(self):
#         return len(self.transactions)


# history = TransactionHistory()

# history.add_transaction("Deposited 5000")
# history.add_transaction("Withdrawn 1000")
# history.add_transaction("Deposited 2000")

# print(len(history))  # history.__len__()
"""Python interally does history.__len__()"""

# ==================== __eq__() =======================
"""
__eq__() allows us to define how two objects should be compared using the == operator.
"""


# class BankAccount:
#     def __init__(self, account_number, owner):
#         self.account_number = account_number
#         self.owner = owner

#     def __eq__(self, other):
#         return self.account_number == other.account_number


# account1 = BankAccount(101, "Maaz")
# account2 = BankAccount(101, "Maaz")
# account3 = BankAccount(102, "Jason")

# print(account1 == account2)  # account1.__eq__(account2) # memory
# print(account2 == account3)


# ======================== Add ===========================
# class ComplexNumber:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, other):  # self: z1, other: z2
#         real_part = self.real + other.real
#         imaginary_part = self.imaginary + other.imaginary

#         return ComplexNumber(real_part, imaginary_part)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"


# z1 = ComplexNumber(10, 20)
# z2 = ComplexNumber(1, 3)


# result = z1 + z2  # z1.__add__(z2)

# print("Complex Number is: ", result) # result.__str__()


# ======================= __call__() method =============================

"""
The __call__() method allows us to call an object just like we call a normal function.
"""


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __call__(self):
#         print("=" * 50)
#         print(f"{self.owner}'s current balance: ₹{self.balance}")
#         print("=" * 50)


# account = BankAccount("Maaz", 5000)

# account()  # account.__call__()

""" Internally it does account.__call__()"""


# class Calculator:
#     def __call__(self, a, b):
#         print("=" * 50)
#         print(f"{a} + {b} = {a + b}")
#         print("=" * 50)


# calculator = Calculator()

# calculator(10, 20)  # calculator.__call__(10, 20)


# ====================== __lt__() and __gt__() =======================
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __lt__(self, other):
#         return self.balance < other.balance

#     def __gt__(self, other):
#         return self.balance > other.balance


# account1 = BankAccount("Maaz", 5000)
# account2 = BankAccount("Jason", 3000)

# print(account1 < account2)
# print(account1 > account2)


# ======================== Reflected Addition ===========================
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __radd__(self, other):  # acccount, other: 1000
#         return other + self.balance  # 1000+ account.balance (1000)


# account = BankAccount(1000)
# # account1 + account2
# print(1000 + account)  # 1000.__add__(account) # account.__radd__(1000)

"""
1000.__add__(account) 1000: int and account: object

there python tries the reflected addition

account.__radd__(1000)

# Therefore the self: account and other: 1000
 Now the function does other + self.balance which becomes 1000 + self.balance and returns it
"""


# ========================= In Place Addition =============================

# age = 21

# age += 10 # age = age + 10
# print(age)


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __iadd__(self, amount):  # self: account, amount: 1000
#         self.balance = self.balance + amount  # self.balance = 5000 + 1000 = 6000
#         return self  # account


# account = BankAccount(5000)

# account += 1000  # account.__iadd__(1000)
# print(account.balance)


# =================== __bool__() ========================

# print(bool(10))

# print(bool(0))

# print(bool("Hello"))

# print(bool(""))


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance


# account = BankAccount(0)
# print(bool(account))


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __bool__(self):
#         return self.balance <= 0


# account = BankAccount(100)
# print(bool(account))

# if account:
#     print("Insufficient Balance")
# else:
#     print("Sufficient Balance")


# =========================== __contains__() ==============================

# numbers = [10, 20, 40, 50]

# print(10 in numbers)
# print(20 in numbers)
# print(30 in numbers)


# class TransactionHistory:
#     def __init__(self):
#         self.transactions = []

#     def add_transaction(self, transaction):
#         self.transactions.append(transaction)

#     def __contains__(self, amount):
#         return amount in self.transactions


# history = TransactionHistory()

# history.add_transaction(500)
# history.add_transaction(1000)
# history.add_transaction(4000)

# print(500 in history)
# print(4000 in history)
# print(5000 in history)


# ========================= __getitem__() =============================
"""
__getitem__() allows us to access elements of a custom object using square brackets []
"""


# class TransactionHistory:
#     def __init__(self):
#         self.transactions = []

#     def add_transaction(self, transaction):
#         self.transactions.append(transaction)

#     def __getitem__(self, index):
#         if 0 <= index < len(self.transactions):
#             return self.transactions[index]
#         else:
#             return "No transaction exists at this location."


# history = TransactionHistory()

# history.add_transaction(500)
# history.add_transaction(1000)
# history.add_transaction(4000)

# print(history[0])
# print(history[1])
# print(history[2])
# print(history[3])


# ========================== __setitem__() =========================
"""
__setitem__() allows us to modify elements of a custom object using square brackets.
"""


# class TransactionHistory:
#     def __init__(self):
#         self.transactions = []

#     def add_transaction(self, transaction):
#         self.transactions.append(transaction)

#     def __getitem__(self, index):
#         if 0 <= index < len(self.transactions):
#             return self.transactions[index]
#         else:
#             return "No transaction exists at this location."

#     def __setitem__(self, index, value):
#         if 0 <= index < len(self.transactions):
#             self.transactions[index] = value
#             return "Value set successfully"
#         else:
#             return "Nothing exists at the given index.Skipping..."


# history = TransactionHistory()

# history.add_transaction(500)
# history.add_transaction(1000)
# history.add_transaction(4000)

# print(history[0])
# print(history[1])
# print(history[2])
# print(history[3])

# history[2] = 2000

# print(history[0])
# print(history[1])
# print(history[2])
# print(history[3])
