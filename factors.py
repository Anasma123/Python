n=int(input("enter the number:"))
fact=[]
for i in range(1,n+1):
    if n%i==0:
        fact.append(i)
print("factors of",n,"are:",fact)
