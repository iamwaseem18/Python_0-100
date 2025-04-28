class employee:
    a=1
    @classmethod            #Instead of showing instance attribute 45 it will show class attribute 1 
    def show(cls):
        print(f'Class Attribute of the employee is {cls.a}')

e = employee()

e.a= 45

e.show()