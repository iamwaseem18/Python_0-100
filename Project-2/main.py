import random
n = random.randint(1,100)
a = -1
guesses = 1
while( a != n):
    a = int(input("Enter a number "))
    if(a>n):
        print("Enter a lower number")
    else:
        print("Enter a higher number")
    guesses +=1
    
print(f"You have entered the correct number {n} in {guesses} attempt")