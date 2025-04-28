a = int(input("Enter your first number "))
b = int(input("Enter your second number "))

if(b == 0):
    raise ZeroDivisionError ("Hey our program is not meant to divide a number by zero")
else:
    print(f"The division of the number a/b is {a/b}")