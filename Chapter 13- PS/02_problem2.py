#Write a program to input name, marks and phone number using format function

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))

s = "The name of the student is {}, His marks are {} and his phone number is {}".format(name,marks,phone)

print(s)