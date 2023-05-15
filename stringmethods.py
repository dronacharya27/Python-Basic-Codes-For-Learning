#Strings are immutable
a="!!Dron!!! Dron!!!!"
print(a.upper())
print(a.lower())
print(a)
#removes anything mentioned from behind only
print(a.rstrip("!"))
#replace
print(a.replace("Dron","Yash"))
#splits and creates a list from mentioned
print(a.split(" "))
#converts first to uppercase and others lower
head = "introduction tO pYthon"
print(head.capitalize())
#centeralize by adding space
print(head.capitalize().center(50))

#returns true if mentioned is ending with string
print(head.capitalize().endswith("python"))

#finds and returns first appearing string
str1= "Hello I am Dron and I am a programmer"
print(str1.find("I"))
#index : rturns error if not found string

print(str1.islower())
print(str1.isalnum())
print(str1.isalpha())
print(str1.isspace())
print(str1.swapcase())
print(str1.title())






