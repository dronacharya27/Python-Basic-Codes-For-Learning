a=int(input("Enter any value between 6 and 9"))
if(a<6 or a>9 ):
    raise ValueError("Value betwwen 6 and 9")
if(a.isalpha):
    raise TypeError("No strings allowed")

