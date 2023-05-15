questions=("What is 1+10","What is Capital of India","Current PM of India")
options=("a.11 \tb.15 \nc.5 \td.60","a.Gujarat \tb.Punjab \nc.Delhi \td.UP","a.Aap \tb.Hum \nc.Modiji \td.koi nahi")
answers =("a","c","c")
amount=0
x=True
while(x==True):
    print("Swagat hai aap sabka KBC mai.\nKhelne ke liye Enter Dabaye.\nKhel band karne ke liye X dabaye.")
    inp=input()
    if(inp=="x"):
        x=False
    else:
        for i in range(len(questions)):
                print("Question" ,i+1 ,questions[i], "\tAmount",(i+1)*100)
                print(options[i])
                ans=input()
                if(ans==answers[i]):
                    print("Sahi jawab!")
                    amount=amount+(i*100)
                    print("Your Winnning:",amount)
                else:
                    print("Galat Jawab!")
                    x=False
                    break
                    
    