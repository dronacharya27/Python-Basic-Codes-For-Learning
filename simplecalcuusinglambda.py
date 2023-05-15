add = lambda x,y: x+y
sub = lambda x,y: x-y
mul = lambda x,y: x*y
div = lambda x,y: x/y
a=input("Enter number A")
b=input("Enter number B")
def main(fx,fx2,fx3,fx4,a,b):
    print("1.ADD,2.SUB,3.MUL,4.DIV")
    c=input()
    match c:
            case 1:
                return fx(a,b)
            case 2:
                return fx2(a,b)
            case 3:
                return fx3(a,b)
            case 4:
                return fx4(a,b)
main(add,sub,mul,div,a,b)
add(a,b)
        
