import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
hour=time.strftime('%H')

if(int(hour)<12):
    print("Good Morning")
elif(int(hour)>12 and int(hour)<16):
    print("Good Afternoon")
elif(int(hour)>16 and int(hour)<20):
    print("Good Evening")
else:
    print("Good Night")