col = {1,2,3,4,5}
print(col)
print(type(col))

# Empty set
colg = set()
print(type(colg))

# --------- Sets Methods ------------

# set.add(): it adds an element
col.add(9)
col.add(7)
print(col)

# set.remove(): it remove an element
col.remove(7)
print(col)

# set.clear(): clears all the set
col.clear()
print(col)

# set.pop(): clears random value in set
coli = {1,2,3,4}
coli.pop()
print(coli)

# sets union
set1 = {1, 2, 3, 4}
set2 = {4,7,8,9}
print(set1.union(set2))

#sets intersection
print(set1.intersection(set2))

