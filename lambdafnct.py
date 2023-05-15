# anonymous functions without name and single lined functions
def double(x):
    return x*2
def appl(fx, value):
    return(fx(value)+26)

double = lambda x:x*2
cube = lambda x: x*x*x

print(double(5),cube(5))
print(appl(double,5))
 
 