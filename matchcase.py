x = int(input("enter a number"))
match x:
    case 0:
        print("x is zero")
#  _ defines default value
    case _ if x==23:
        print(x,"is 23")

    # case _ if(type(x)==str):
    #     print("X is string")
    case _:
        print("randomnumber")