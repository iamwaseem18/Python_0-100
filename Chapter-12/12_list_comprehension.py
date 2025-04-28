# It is the most elegant way to create a list using another list

myList = [2,4,8,5,9,0]

squaredlist = []
for item in myList:
    squaredlist.append(item*item)

print(squaredlist)

#Using List Comprehension

squaredlist = [i*i for i in myList]

print(squaredlist)