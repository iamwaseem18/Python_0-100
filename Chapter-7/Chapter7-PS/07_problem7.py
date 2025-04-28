#Write a program to create a star pattern where n = 3

n = int(input("Enter a number"))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")