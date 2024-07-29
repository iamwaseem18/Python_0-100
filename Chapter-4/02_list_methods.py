# There are various methods used on lists.
# 1) Sort Method. It is used to sort the order of  the list in increasing or decreasing order

number=[1,2,4,9,6,8]

number.sort()  #Ascending order
print(number)


number.sort(reverse=True) #Descending order
print(number)

# 2) It is used to reverse the given list

number.reverse()
print(number)
#  3) It is used to add an element at the end of the list

number.append("Harry")
print(number)

# 4) It is used to add any data at any give index
friends=["Apple","karyapak", 34,3.098, False,"Rohan","Akaash"]

friends.insert(3,"waseem") # it has added waseem at index 3

print(friends)

#5) It is used to remove any element from any index in a list

friends.pop(2)
print(friends)

# If you want to return the popped out vale you can simply write

print(friends.pop(2))

# We can also write
value = friends.pop(2)
print(value)

#6) Instead of specifying index we can directly use value to remove it from string

friends.remove("Akaash")
print(friends)

