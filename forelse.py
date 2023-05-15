for i in range(10):
    print(i)
else:
    print("No i")
    
for i in []:
    print(i)
else:
    print("no i")

#working of else is not breaking but finishing of loop, success

for i in range(5):
    print(i)
    if i ==0:
        break
else:
    print(" no print")