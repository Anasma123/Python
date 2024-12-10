a=int(input("enter the first numnber:"))
b=int(input("enter the second number"))
c=int(input("enter the third number:"))
def num(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)
num(a,b,c)
        
