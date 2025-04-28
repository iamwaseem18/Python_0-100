'''A function is a group of statements performing a specific task. 

When a group gets bigger and bigger in size and its complexity grows, it gets difficult for the a program to keep track on which peice of code is doing what

A function can be used in a program any number of times'''

#Function Definition:
def avg():
    a = int(input("Enter your first number"))
    b = int(input("Enter your second number"))
    c = int(input("Enter your third number"))

    average = (a+b+c)/3
    print(average)

#Function Call:
avg()    



#Write a program to greet a user with "Good Day" using functions

def greet():
    print("Good Day")

greet()    