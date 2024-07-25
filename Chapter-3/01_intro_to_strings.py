name = "waseem"

# The above written word waseem in quotes is called as string and it is stored
# in the variable name

# String is immutable datatype- Which means we cannot change a single character of string

print(len(name)) #length of the string

# Indexing and Slicing of string

nameshort= name[0:3] #Start from index 0 all the way till index 3 (excluding 3)

print(nameshort)

character = name[1] #Only sliced one character

print(character)
nameshort1= name[-4:-1] #Start from index 0 all the way till index 3 (excluding 3)

print(nameshort1)

# Some more ways of slicing

print(name[:])

print(name[1:])

print(name[:4])


a = "0123456789"
print(a[1:8:2]) #First we will take legth from 1-8(1234567) 
# Then it will slice the o/p by the length of two and we get(1357)