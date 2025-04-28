class employee:
    a=1
    @classmethod            #Instead of showing instance attribute 45 it will show class attribute 1 
    def show(cls):
        print(f'Class Attribute of the employee is {cls.a}')

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a= 45

e.name = "Waseem Khan"
print(e.fname, e.lname)

e.show()