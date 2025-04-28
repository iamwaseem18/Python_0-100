a = int(input("Enter a number "))

table = [a*i  for i in range(1,11) ]

with open("table.py","a") as f:
    f.write(f"Table of {a}: {str(table)} \n")