l = [3,353,45,6564]

index = 0
for item in l:
    print(f"The item number at index{index} is {item}")
    index += 1


#The above program can be simplified using Enumerate function

for index,item in enumerate(l):
    print(f"The item number at index{index} is {item}")