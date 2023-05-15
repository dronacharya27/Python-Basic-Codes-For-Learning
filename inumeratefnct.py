marks=[12,35,25,16,78,65]
index=0
for mark in marks:
    print(marks)
    if(index==3):
        print("heello")

for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("using enamurate")