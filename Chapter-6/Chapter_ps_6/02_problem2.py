a = int(input("Enter the marks for English "))
b = int(input("Enter the marks for Maths "))
c = int(input("Enter the marks for Science "))

#Check for total subject pass percentage
total_percentage = ((100)*(a + b + c))/300

if(total_percentage >= 40):
    print("Student has passed the combined pass criteria")

else:
    print("Student has not passed the combine marks criteria")

#Check for individual subject pass percentage
if(a and b and c >= 33):
    print("Student has passed the individual pass criteria")    

else:
    print("Student has not passed the combined pass criteria") 

print("End of the program and your total percentage is:", total_percentage)       