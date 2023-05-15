name=("dron","henil","yash")
temp = list(name) #conver to list
temp.append("parth") #add item
temp.pop(0)     #remove item
temp[1]="Bhaskar" #change
name = tuple(temp) #convert back
surname=("patel","gaurav","bhau bhau")
fname=name+surname
print(fname)
number=(1,2,3,3,5,8,3,2)
print(number.count(3))
print(number.index(3,4,)) #for finding in specific range