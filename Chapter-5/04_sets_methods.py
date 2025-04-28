# 1) update the values in the set

s = {1,2,4,5,9}
s.add("Waseem")
print(s)

# O/p: {'Waseem', 1, 2, 4, 5, 9}

# methods on sets

s={1,2,3,4}

# len(s) returns 4
# s.remove(2) removes 2 from the set
# s.pop() removes a random element from the set
# s.clear() empties the set
# s.union({8,11}) creates a new set with all the values in the both set
# s.intersection({8,11}) creates a new set with identical values in both set

# Example for union and intersection

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = (s1.union(s2))
print(s3)

# o/p {1, 2, 3, 4, 5, 6, 7, 8}

s4 = (s1.intersection(s2))
print(s4)
# o/p {4, 5}