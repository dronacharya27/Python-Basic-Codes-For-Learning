# f= open('myfile.txt','r')
# # print(f)
# text=f.read()
# print(text)
# f.close()

# f= open('myfile2.txt','a')
# f.write('Hello World')
# f.close()
# with open('myfile.txt','a') as f:
#     f.write("using with")
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} is:{m1}")
    print(f"Marks of student {i} is:{m2}")
    print(f"Marks of student {i} is:{m3}")
    print(line)