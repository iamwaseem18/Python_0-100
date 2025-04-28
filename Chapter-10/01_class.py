class employee:
    language = "Python" #This is an class attribute    
    salary = 1200000

Harry = employee()
Harry.name = "Harry" #This is an instance attribute
print(Harry.name, Harry.language, Harry.salary)    

Rohan = employee()
Rohan.name = "Rohan"
print(Rohan.name, Rohan.salary, Rohan.language) 

# Here name is instance attribute and Salary and language are class
# attributes as they directly belong to class 