#Create a class programmer where we can store data of employees working in microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary =  salary
        self.pin = pin


W = Programmer("Waseem",130000,32301)
print(W.name, W.salary, W.pin, W.company) 
R = Programmer("Rohan",130000,32301)       
print(R.name, R.salary, R.pin, R.company)      