class person:
    name = "Dron"
    occupation = "Developer"
    def info(self):
        print(f"{self.name} is a {person.occupation}")

a = person()
b= person()
a.name = "Henil"
a.occupation = "student"
a.info()
b.info()