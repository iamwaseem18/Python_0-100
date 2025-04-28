# Instead of zerodivision error, print infinite

try:
    a = int(input("Enter your first number a: "))
    b = int(input("Enter your second number b: "))
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite Value")