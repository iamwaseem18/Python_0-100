# Inheritence is the way of creating a new class from an existing class

class Employee:
    company = "ITC"             #This is called as parent class

    def show(self):
        name = "Waseem"
        salary = 10000
        print(f"The name of the Employee is {name} and the salary of the employer is {salary}")


class coder:
    company = "Prism"

    def mask(self):
        language = "Python"
        print(f"My favourite language is {language}")

class programmer(Employee,coder):                 #This is called as inherited class
    company = "ITC InfoTech"

    def showlanguage(self):
        name = "waseem"
        print(f"The name of the employee is {name}")



a = Employee()

b = coder()

c = programmer()

c.show()
c.mask()
c.showlanguage()