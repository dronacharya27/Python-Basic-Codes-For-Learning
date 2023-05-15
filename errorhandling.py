
try:
    a= int(input("Enter a number:"))
    print(f"Multiplication Table of {a} is:")

    for i in range(1,11):
        print(f"{a}X{i}={a * i}")
except:
    print("Invalid input")
print("need to print")

try:
    num=int(input())
    a=[1,4]
    print(a[num])
except ValueError:
    print("No a integer")
except IndexError:
    print("Index error")
