import random

comp = int(random.randint(0,2))
winmatrix= [[2,0,1],[1,2,0],[0,1,2]]

user = int(input("0 For Rock \n1 For Paper \n2 For Scissors"))

def compfunction(comp):
    if(comp==0):
        print("ROCK")
    elif(comp==1):
        print("PAPER")
    else:
        print("SCISSORS")

def userfunction(user):
    if(user==0):
        print("ROCK")
    elif(user==1):
        print("PAPER")
    else:
        print("SCISSORS")
        
def maincheck(comp,user):
    if(winmatrix[user][comp]==1):
            print("YOU WON")
    elif(winmatrix[user][comp]==0):
            print("YOU LOSE")
    else:
            print("DRAW")
print("You Chose:")
userfunction(user)
print("Computer Chose:")
compfunction(comp)
maincheck(comp,user)
