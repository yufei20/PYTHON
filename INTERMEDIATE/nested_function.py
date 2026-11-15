#TYPEHINTING CONCEPT

def outer()-> None:   # ye matlab function will return nothing, it is called "typehinting"
    print("outer function")
    
    def inner():                            # local function hai ye, cannot be accessed outside
        print("I'm inner function")
    
    inner()       # ye hogya function call
    
    print("outer funtion is completed")
    
#===============================================================
#DOCSTRING CONCEPT

def outer(age: int, name: str)-> bool:

  """
  This function will compare age and tell if a persson is eligible for driving

  Args:
      age: int  This will take persons age
      name: str This will take persons name

  Returns:
      bool:  True or False if person is eligible or not
  
  """
    print(f"My name is {name} and age is :{age} years old")
    
    def inner()->bool:                            
        print("this function will compare age")
        if age > 18:
            return True
        return False
        
    
    can_drive = inner()      
    
    print("outer funtion is completed")
    return can_drive
    

a = int(input("Enter your age-> "))
outer(a,"jyoti")

        
