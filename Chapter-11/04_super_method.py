class employee:
    def __init__(self):
        print("Constructor of the Employee")
   
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of the programmer")
    b = 2

class Manager(programmer):
    def __init__(self):
            super().__init__()
            print("Constrctor of the Manager")
    c = 3


o = Manager()    
print(o.a,o.b,o.c)