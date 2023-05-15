def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank YOu for using this function")
    return mfx

@greet
def hello():
    print("HEllo World")
hello()

@greet
def add(a,b):
    print(a+b)

add(2,4)