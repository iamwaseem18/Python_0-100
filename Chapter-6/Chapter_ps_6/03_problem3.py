s1="Make a lot of money"
s2= "Buy now"
s3= "Subscribe This"
s4= "Click this"
message = input("Enter your Email Title:" )
if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message) ):
    print("Spam email")

else:
    print("Not a spam email")    