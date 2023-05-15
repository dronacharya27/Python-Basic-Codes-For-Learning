s1={1,2,3,3}
s2={3,4,5,6,4}
print(s1.union(s2)) #o get union
print(s1,s2)
s1.update(s2) #to update with unnion 
print(s1)
print(s1.intersection(s2)) #to intersect
s3={5,3}
s1.intersection_update(s3) #to intersect with update
print(s1)
print(s1.symmetric_difference(s2))
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.add(69)
s1.remove(5)
# s1.clear()
del s2
s1.pop()
