# f = open("file.txt")
# print(f.read())
# f.close()


#The above process can be done using "with" stmt

#You dont have to explicitly close the file


with open("file.txt") as f:
    print(f.read())