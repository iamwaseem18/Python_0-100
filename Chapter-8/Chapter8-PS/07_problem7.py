# Write a program to strip an from the list
l= ["Shubham","Harry","Anas","as"]

def rem(l,word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


print(rem(l,"as"))