def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n* fact(n-1))
num=int(input("enter a number:"))
print("number is:",num)
print("factorial is:",fact(num))
