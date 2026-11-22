"""Method Resolution Order (MRO) is the sequence in which a programming language searches classes for a method or attribute across an inheritance hierarchy"""

class Person:                #class1

  def __init__(self,name,age):
    self.name = name
    self.age = age
    print(f" Person {self.name} is {self.age}yrs old ")

class Staff(Person):                 #class2 inheriting class1

  def __init__(self,name,age,staff_id,salary):
    super().__init__(name,age)
    self.staff_id = staff_id
    self.salary = salary

class Doctor(Staff):                    #class3 inheriting class2

  def __init__(self,name,age,staff_id,salary,speciality,yoe):
    super().__init__(name,age,staff_id,salary)
    self.speciality = speciality
    self.yoe = yoe
    print(f"{self.name} is {self.age}yrs old and has {self.yoe} years of experience.\n Salary is {self.salary}\n Speciality is {self.speciality}" )

person1 = Doctor("carron",23,10111,70000,"dermatologist",10)
