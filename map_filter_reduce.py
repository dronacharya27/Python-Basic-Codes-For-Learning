from functools import reduce
l = [1,2,3,4,5,6]
ml= list(map(lambda x:x*x,l))
print(ml)

fl= list(filter(lambda x:x>3,l))
print(fl)
def mysum(a,b):
    return a+b

# Reduce [1,2,3,4,5,6] it will add two numbers 
# and do it untill reaches the last number and 
# will give the final remaining digit as output
f3= reduce(lambda x,y:x+y,l)
print(f3)