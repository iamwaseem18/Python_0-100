# Write a multiplication table using list comprehension

a = int(input("Enter a number "))

table = [a*i  for i in range(1,11) ]
print(table)