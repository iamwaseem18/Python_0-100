# Write a program to greet people whos name starts with s in the list l

l=["Harry","Soham","Sachin","Rahul"]

for names in l:
    if(names.startswith("S")):
        print(f"Hello {names}")