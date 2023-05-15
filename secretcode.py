import random
import string
randnum=random.choices(string.ascii_lowercase,k=3)

entry = input("Enter The String:")
list=entry.split(" ")
list1=[]
list2=[]
for i in list:
    if(len(i)<=3):
            for j in i:
                list1.append(j)
                list1.reverse() 
    else:
        for j in i:
            list1.append(j)
        a=list1.pop(0)
        list1.extend(a) 
        for i in range(3):
            list1.insert(i,randnum[i])
            list1.extend(randnum[i])
    
Encode=""
for i in list1:
    Encode=Encode+i
print(Encode)

    

    
        
        