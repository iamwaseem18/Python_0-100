#Create an empty dictionary. Allow 4 friends to enter their faviorate language as value and use key as their names. Assume that names are unique

w={}

name = input("Enter your name : ")
language = input("Enter your language: ")

w.update({name:language})

name = input("Enter your name : ")
language = input("Enter your language: ")

w.update({name:language})

name = input("Enter your name : ")
language = input("Enter your language: ")

w.update({name:language})

name = input("Enter your name : ")
language = input("Enter your language: ")

w.update({name:language})

print(w)
