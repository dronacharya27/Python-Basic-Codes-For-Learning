print("💖WELCOME TO FLAMES💖\n")
name1=input("💞Enter Your Name💞\n")
name2= input("💕Enter Your Lover Name💕\n")
name1l=[]
name2l=[]
for x in name1:
    name1l.append(x)
for x in name2:
    name2l.append(x)
    

for x in name1l: 
    for y in name2l:
        if(x==y):
            name1l.remove(y)
            name2l.remove(y)
            
           
print(name1l)
print(name2l)           

list1=name1l+name2l

if(len(list1)==1 or len(list1)==6):
    print("👬YOU ARE FRIENDS FOREVER👬")
    
elif(len(list1)==2 or len(list1)==7):
    print("😘YOU ARE LOVERS😘")
    
elif(len(list1)==3 or len(list1)==8):
    print("🥰YOU HAVE AFFECTION🥰")
    
elif(len(list1)==4 or len(list1)==9):
    print("💍YOU ARE GOING TO MARRY💍")
    
else:
    print("😈YOU ARE ENEMIES😈")
    
