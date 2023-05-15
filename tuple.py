tup =(1)
print(type(tup))
tup=(1,2,3,"dron",True)
print(type(tup))
# tup[0]=9 cannot change
print(tup[0])
print(tup[3])
print(tup[4])

if "dron" in tup:
    print("yes")
# slicing will creat new tupple
tup2=tup[1:4]
print("tup2")
