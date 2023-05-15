#finally occurs anyhow whatever happens it occcurs
def main():
    try:
        l=[1,2,3,4]
        i=int(input())
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I always executed")
    print("i always executes")

main()