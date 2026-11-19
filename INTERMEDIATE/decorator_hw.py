#Decorator Homework done for 16th Nov'16

def verify_pin(func):
  def innerwrapper(self,pin,*args):
    if pin == self.pin:
      return func(self,pin,*args)
    else:
      print("incorrect pin")
  return innerwrapper
  

class BankAccount:
  def __init__(self, pin, balance):
    self.pin = pin
    self.balance = balance
    print ("account created successfully")

  @verify_pin
  def withdraw(self, pin, amount):
    if amount >= self.balance or amount < 0:
      print ("invalid amount entered")
    else:
      self.balance= self.balance - amount
      print(f"Rs{amount} has been debited from your account.")

  @verify_pin
  def checkbalance(self, pin)->None:
    print (f"Your current balance is {self.balance}")

  @verify_pin
  def deposit(self, pin, amount):
    if amount < 0:
      print ("invalid amount")
    else:
      self.balance = self.balance + amount
      print(f"Rs.{amount} has been credited to your account.")


yufei = BankAccount(1111, 50000)
yufei.checkbalance(1111)
yufei.deposit(1111, 25)
yufei.withdraw(1111, 2000)
yufei.checkbalance(1111)
jyoti.checkbalance(9999)

===============================================
output:
account created successfully
Your current balance is 50000
Rs.25 has been credited to your account.
Rs2000 has been debited from your account.
Your current balance is 48025
incorrect pin
