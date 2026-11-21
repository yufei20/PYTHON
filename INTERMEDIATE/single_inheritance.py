class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age
    print(f" Person {self.name} is {self.age}yrs old ")

class Doctor(Person):

  def __init__(self,name,age,speciality,yoe):
    super().__init__(name,age)
    self.speciality = speciality
    self.yoe = yoe
    print(f"{self.name} is {self.age}yrs old and has {self.yoe} years of experience" )

person1 = Doctor("carron",23,"dermatologist",10)

====================

output: 
 Person carron is 23yrs old 
carron is 23yrs old and has 10 years of experience
