class Person:

  def __init__(self, name, age):
    self._name = name   # protected instance variable = arg
    self.__age = age #private variable
    self.greet()
    self.ageCheck()

  def greet(self):
    print(f"hello {self._name}")
    
  def ageCheck(self):
    if self.__age <18:
      print("young")
    else:
      print("aged")


###########################calling of class n method
suzi = Person("suzi", 25)

suzi._name = "jyoti" #yaha you changed protected variable value
suzi._Person__age = 17 #yaha you changed private variable value
#priavte variable is changed in this format internally by python and called name mangling

suzi.greet()
suzi.ageCheck()


