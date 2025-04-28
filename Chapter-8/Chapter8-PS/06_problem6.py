# Write a program to convert inches into cms
inc = int(input("Enter the value of inches "))

def size(inc):
    return(inc*2.54)


print(f"centimeter = {size(inc)}")
