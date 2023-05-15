age=int(input("Enter your age:"))
print("Your age is", age)

if(age>18):
    print("You can drive")
else:
    print("You cannot drive")
# Elif

num=int(input("Enter a number:"))
if(num<0):
    print("Numeber is negative")
elif(num==0):
    print("Number is zero")
elif(num==69):
    print("Number is special")
else:
    print("Number is positive")
print("I am Happy")
# Nested

if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=1 and num<=10):
        print("Number is between 1 and 10")
    elif(num>=10 and num<=20):
        print("number between 10 and 20")
    else:
        print("greater than 20")
else:
    print("Number is zero")

