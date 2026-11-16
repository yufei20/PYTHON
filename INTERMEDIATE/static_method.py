#static method and class method
#static method

class TemplateCar:
      """
      This is class for understanding static method with car as class 
      
      """
      def __init__(self)-> None:
        pass

      @staticmethod
      def greet(name:str) -> None:   #isko bina object, class se bhi access kr skte hai
        """
        this method is static. This method prints name of owner

        Args:
          name: str = This takes name of vehicle owner

        Returns:
          None
        """
        print(f"Welcome dear {name}")

      def carEngine(self, model: str) -> None:  
        """
        this method is regular method. This tells the model of engine in car

          Args:
          model: str = This takes model of engine

          Returns:
          None
        """
        print(f"car engine model is {model}") # this is instance method
        


marutisuzuki = TemplateCar() # instance of class
marutisuzuki.carEngine("m35") # this is call by instance/object

TemplateCar.greet("jyoti") 
TemplateCar.carEngine(TemplateCar(), "m45") # this is call by class, instance method is called
