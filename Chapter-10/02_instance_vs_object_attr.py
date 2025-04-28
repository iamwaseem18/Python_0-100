''' Instance attribute, takes prefernce over class attributes during 
    assignment and retrival '''

class Employee:
    language = "Python"
    salary = 12000000

harry = Employee()    
harry.language = "JavaScript"
print(harry.language, harry.salary)

# Here we can see python has categorised instance attribute over class
# class attribute