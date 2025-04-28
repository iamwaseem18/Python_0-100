# Add a static attribute to the question 2 which say hello


class Calculator:
    def __init__(self,n):
        self.n = n

    @staticmethod
    def hello():
         print("hello")

    def square(self):
        print(f"The square is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n }")

    def squareroot(self):
        print(f"The cube is {self.n ** 1/2}")


a = Calculator(4)  
a.hello()      
a.square()
a.squareroot()
a.cube()
