#fact(n)=n*fact(n-1)
def fact(n):
    '''fact(5)
    5*fact(4)
    5*4*fact(3)
    5*4*3*fact(2)
    5*4*3*2*fact(1) which is 1
    5*4*3*2*1
    120'''
    if(n==0 or n==1):
        return 1
    else:
        return (n*fact(n-1))
n=int(input())
fact(n)


def fibbo(n):
    if n==1 or n==0:
        return n
    else:
        return (fibbo(n-1)+fibbo(n-2))  

for i in range(n):
    print(fibbo(i))
