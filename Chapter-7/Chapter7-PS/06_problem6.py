#Find the factorial of the given number

n = int(input("Enter your number"))

product = 1

for i in range(1,n+1):
    product = product * i
   
   
print(f"For the given number {n}, The factorial value is {product}")