# Inheritence is the way of creating a new class from an existing class

class Employee:
    company = "ITC"             #This is called as parent class

    def show(self):
        name = "Waseem"
        salary = 10000
        print(f"The name of the Employee is {name} and the salary of the employer is {salary}")


# If i want to create one more class with same functions and more from the above class then i have to copy everything manually
# Like below


# class programmer:
#     company = "ITC InfoTech"

#     def show(self,name,salary):
#         print(f"The name of the Employee is {name} and the salary of the employer is {salary}")


#     def lang(self, name,language):
#         print(f"The employee name is {name} and the language of the employee is {language}")


# a = Employee()
# a.show("waseem",10000)

# b = programmer()
# b.show("waseem",10000)
# b.lang("waseem","Python")



#Instead of writing all the programmer code we can simply inherit from the employee class like below


class programmer(Employee):                 #This is called as inherited class
    company = "ITC InfoTech"

    def showlanguage(self):
        name = "waseem"
        print(f"The name of the employee is {name}")



a = Employee()

b = programmer()

a.show()