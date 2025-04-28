# Write a program to add first n natural numbers

def sum(n):
    if(n==1):
        return 1
    return (n*(n+1))/2

n = int(input("Enter your greatest number")) 
print(f"The sum of all the natural numbers is {sum(n)}")