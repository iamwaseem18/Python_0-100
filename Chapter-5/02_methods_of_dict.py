marks = {"Harry":90, "Cuban":20, True:90 }
print(marks)

# There are vaious methods which are used to return values from Dictionary

# 1) It returns the list of key and value in form of tuples

print(marks.items())

#Ans: dict_items([('Harry', 90), ('Cuban', 20), (True, 90)])

# 2) It is used to retrive keys from the given dictionary

print(marks.keys())

# Ans: dict_keys(['Harry', 'Cuban', True])

# 3) It is used to retrive values from the given dictonary

print(marks.values())

# dict_values([90, 20, 90])

#4) It is used to update the value in a dictonary or add a new key value pair

marks.update({"Harry":99,"Ritesh":8})
print(marks) 

# 5) It is used to check wheather the given key is present or not 

print(marks.get("Harry")) #99
print(marks.get("Sheetal")) #When a given key name is not present it returns None

# print(marks("Sheetal")) #Where as when done normally returns error

#6 It is used to clear the dictionary

marks.clear()
print(marks)


















