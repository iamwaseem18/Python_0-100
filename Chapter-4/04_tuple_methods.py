# There are various methods used in a tuple

# 1) It is used to count the given data in the tuple. Which tells us how many times is it repeating

a = (1,22,333,333,222,22)

no = a.count(333)

print(no)


# 2) It is used to find the index of the given value

yes = a.index(333)

print(yes)

#3) It is used to add multiple tuples into a single tuple

HI = (1,2,3,4)
LOW = (5,6,7,8)

concatination = HI + LOW

print(concatination)

#4) It is used to multiply the same tuple twice or thrice and print it into a single tuple

Repeated = HI * 3

print(Repeated)


#5) It is used to check wheather the given element is present in the tuple or not

print(2 in HI)
print(5 in HI)

#6) It is used to count the length of the tuple

print(len(HI))


# Slicing and unpacking are some more methods used in tuple very commonly