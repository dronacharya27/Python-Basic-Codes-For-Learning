# Greeting
print("Hello and welcome to Calculator. Enter x to end.")

# Functions
def add(a):
        print(type(a))
        v=0
        for i in range(len(a)):
            v = v + int(a[i])
        print(v)

def sub(a):
        v=0
        for i in range(len(a)):
            if(i==(len(a)-1)):
                break
            v=int(a[i])-int(a[i+1])
        print(v) 

def mul(a):
    v=1
    for i in range(len(a)):
        v= v * int(a[i])
    print("RESULT:",v)           

def div(a):
    v=1
    for i in range(len(a)):
        if(i==(len(a)-1)):
            break
        v= int(a[i]) / int(a[i+1])
    print("RESULT:",v)
 
# Main Calculator
   
run=True 
while(run==True):
    
    value=input()
    
    
    if(value=="x"):
        run=False
    elif(value.isalpha() and value.isalnum()):
        print("Invalid")
    else:
        for x in value:
            
            if(x=="+" or x=="-" or x=="*" or x=="/" or x=="%"):
                list2=value.split(x)
            
                   
                match x:
                    case "+":
                        add(list2)
                        break
                        
                    case "-":
                        sub(list2)
                        break

                    case "*":
                        mul(list2)
                        break

                    case "/":
                        div(list2)
                        break
                    
                    # case "%":
                    #     for i in range(len(list2)):
                    #         v= v % int(list2[i])
                    #     print("RESULT:",v)
                    #     break

            
                    
    
    
            
        

   