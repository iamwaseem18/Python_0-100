#Find out the line number where "Python" is present in prblm6

with open("log.txt") as f:
    lines = f.readlines()


lineno = 1

for line in lines:
    if("python" in line):
        print(f"Python is present in {lineno}")
        break
    lineno += 1 

else:
    print("No python is not present in the file")    