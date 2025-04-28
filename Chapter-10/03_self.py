class employee:
    language = "Python"
    Salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.Salary}")

    @staticmethod  #As we have added this method here we do not need to pass self
    def greet():
        print("Good Morning")


harry = employee()
harry.language = "JavaScript"

harry.greet()
harry.getinfo()
# employee.getinfo(harry)
