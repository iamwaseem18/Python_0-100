# Write a program to check whether the word twinkle is present in the file poem.txt or not

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")    

f.close