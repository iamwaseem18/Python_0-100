# Write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce

l = [1,22,555,675,777,8995,880]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))