class Employee:
    salary = 10000
    increment = 20
    def show(self):
        print(f"The Past Salary of the employee is {self.salary}")

    @property
    def Salaryafterincrement(self):
        return(self.salary +self.salary * (self.increment/100) )
    
    @Salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
e.show()
print(e.Salaryafterincrement)
e.salaryafterincrement = 13000
print(e.increment)