# Write a program to convert celsius into Fareinheat 

def temp(c):
    return ((c * 1.8) + 32)

c = int(input("Enter the number: "))
print(f"The temperature in farenheat is {round(temp(c),2 )}")
