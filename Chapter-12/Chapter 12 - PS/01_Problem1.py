# Write a program to open multiple text files. If no file exist a message without exiting the 
# program should appear
try:
    with open("1.txt","r") as f:
        print(f.read()) 
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:    
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank You!!!")

