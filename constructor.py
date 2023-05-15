class person:
    def __init__(self,n , o):
        print("Hey i am a person")
        self.name = n 
        self.occupation = o
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("Dron" , "Student")
b= person("Henil" , "Developer")
a.info()
b.info()
# a.name = "henil"
# a.occupation = "Student"
# a.info()
