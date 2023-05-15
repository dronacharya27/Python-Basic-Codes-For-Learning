# ORDERED 
marks=[5,6,7,"MATHS",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-1])
# positive index = length(list) - negative index
# print(marks[1:-1])=print(marks[1:4])
# Methods
if 4 in marks:
    print('yes')
else:
    print('false')
    
# String matching 
if "ro" in "Dron":
    print('yes')
    
# Jump indexing
print(marks[0:len(marks)])
print(marks[0:5:2])

# List comprehension
lst =[i*i for i in range(10)]
print(lst)
lst =[i for i in range(10) if i%2==0]
print(lst)


