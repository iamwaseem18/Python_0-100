# Print 3,5,7 element using enumerate function

l = [1,2,3,4,5,6,7,8,9,10]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
         print(f"The item number at index {i} is {item}")