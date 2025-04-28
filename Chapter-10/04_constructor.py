class employee:
    language = "Python"
    Salary = 1200000

    def __init__(self,name,Salary,language): #This is a dunder method. It calls itself automatically. 
        self.name = name
        self.Salary = Salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.Salary}")

    @staticmethod  #As we have added this method here we do not need to pass self
    def greet():
        print("Good Morning")

harry = employee("Harry",130000, "JS")
# harry.name = "Waseem"
print(harry.name, harry.Salary,harry.language)

