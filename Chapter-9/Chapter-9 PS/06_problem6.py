# Check wheather the word python is present in log.txt

with open("log.txt","r") as f:
    content = f.read()

if ("python" in content):
    print("Python is present")    

else:
    print("Python is not present")
