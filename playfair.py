import numpy

a=numpy.empty(5,5)
    

for i in range(4):
    for j in range(4):
            a[i,j]=i

print(a)